#!/usr/bin/env python3
"""Equalang from the command line: translate files, transcribe recordings, translate text.

One command per thing to do, each carrying the whole job through: upload the
file (or hand Equalang its URL), wait, write the results beside the source,
print where they are. The agent running this never builds a multipart body or
a polling loop, and never sees the file's bytes -- which would cost a fortune
in context to say nothing.

Standard library only: it runs wherever Python 3.8+ does, with nothing installed.

    export EQUALANG_API_KEY=el_...
    python3 equalang.py estimate report.pdf
    python3 equalang.py translate report.pdf --to zh-CN
    python3 equalang.py transcribe interview.mp3 --format srt --format txt
    python3 equalang.py text "Good morning." --to ja

Every command prints one JSON object on stdout; progress goes to stderr. A
failure prints {"error", "code", "retryable"} and exits 1.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
import uuid
from pathlib import Path
from urllib import error, request

VERSION = '0.1.0'
SITE = 'https://equalang.com'
KEYS_URL = f'{SITE}/api-keys'
MAX_UPLOAD_BYTES = 100 * 1024 * 1024
ATTEMPTS = 3
# A command line has no client timing it out, so it waits for the job; an
# interrupted wait does not cancel the job, which `status` picks up again.
DEFAULT_TIMEOUT_SECONDS = 1800


class EqualangError(Exception):
    """A failure worth showing as it is: what happened, and whether trying again can help."""

    def __init__(self, message, code='', retryable=False, data=None):
        super().__init__(message)
        self.code, self.retryable, self.data = code, retryable, data or {}


def _api_key():
    key = (os.environ.get('EQUALANG_API_KEY') or '').strip()
    env_file = Path(__file__).resolve().parent.parent / '.env'
    if not key and env_file.exists():
        for line in env_file.read_text(encoding='utf-8').splitlines():
            name, _, value = line.partition('=')
            if name.strip() == 'EQUALANG_API_KEY':
                key = value.strip().strip('"').strip("'")
    if not key:
        raise EqualangError(
            f'No API key. Ask the user for one, or to create one at {KEYS_URL}; then `export EQUALANG_API_KEY=el_...` '
            'or put it in this skill\'s .env. Never invent a key.', 'MISSING_API_KEY')
    return key


def _base_url():
    return (os.environ.get('EQUALANG_BASE_URL') or f'{SITE}/v1').rstrip('/')


def _call(method, path, *, body=None, content_type=None, creates=False, keyless=False):
    """One request, sent again only when that is safe and can help.

    The API says which failures those are (`retryable`) and how long to wait
    (Retry-After). A request that creates something carries one
    Idempotency-Key across its attempts: the retry of a request whose answer
    was lost finds the job the first attempt made, instead of making -- and
    charging for -- a second.

    Returns:
        tuple: (data, headers) of the unwrapped envelope.
    """
    headers = {'User-Agent': f'equalang-skill/{VERSION}'}
    if not keyless:
        headers['Authorization'] = f'Bearer {_api_key()}'
    if content_type:
        headers['Content-Type'] = content_type
    if creates:
        headers['Idempotency-Key'] = str(uuid.uuid4())
    failure = None
    for attempt in range(1, ATTEMPTS + 1):
        try:
            with request.urlopen(request.Request(f'{_base_url()}{path}', data=body, method=method, headers=headers), timeout=300) as response:
                return json.loads(response.read()).get('data'), response.headers
        except error.HTTPError as exc:
            try:
                envelope = json.loads(exc.read())
            except ValueError:
                envelope = {}
            message = str(envelope.get('message') or exc.reason)
            if exc.code == 401:
                message += f' Check EQUALANG_API_KEY, or create a key at {KEYS_URL}.'
            if exc.code == 402:
                message += f' Top up at {SITE}/pricing.'
            failure = EqualangError(message, str(envelope.get('code') or f'HTTP_{exc.code}'),
                                    bool(envelope.get('retryable', exc.code >= 500)), envelope.get('data'))
            if not failure.retryable or attempt == ATTEMPTS:
                raise failure from exc
            time.sleep(min(float(exc.headers.get('Retry-After') or attempt), 20))
        except error.URLError as exc:
            failure = EqualangError(f'cannot reach {_base_url()}: {exc.reason}', 'NETWORK', True)
            if method != 'GET' and not creates:
                raise failure from exc
            time.sleep(attempt)
    raise failure or EqualangError('the request was not sent', 'NETWORK', True)


def _multipart(fields, path):
    """A multipart body of the form fields and one file part named `file`."""
    if not path.is_file():
        raise EqualangError(f'no such file: {path}', 'FILE_NOT_FOUND')
    if path.stat().st_size > MAX_UPLOAD_BYTES:
        raise EqualangError(f'{path.name} is {path.stat().st_size / 1048576:.1f} MB; the limit is {MAX_UPLOAD_BYTES // 1048576} MB', 'FILE_TOO_LARGE')
    boundary = f'----equalang{uuid.uuid4().hex}'
    parts = [f'--{boundary}\r\nContent-Disposition: form-data; name="{name}"\r\n\r\n{value}\r\n'.encode()
             for name, value in fields.items() if value is not None]
    name = path.name.replace('"', '')
    parts.append(f'--{boundary}\r\nContent-Disposition: form-data; name="file"; filename="{name}"\r\n'
                 f'Content-Type: application/octet-stream\r\n\r\n'.encode() + path.read_bytes() + b'\r\n')
    return b''.join(parts) + f'--{boundary}--\r\n'.encode(), f'multipart/form-data; boundary={boundary}'


def create_job(task, source, *, file_id=None, target=None, source_language=None, options=None):
    """Start a job from bytes on this machine, a public URL, or an uploaded file.

    A URL is handed to the API, which fetches it itself: nothing is downloaded
    here only to be uploaded again.
    """
    options = {key: value for key, value in (options or {}).items() if value not in (None, [], False)}
    fields = {'target_language': target if task == 'translate' else None, 'source_language': source_language}
    if file_id or source.lower().startswith(('http://', 'https://')):
        named = {'file_id': file_id} if file_id else {'file_url': source}
        body = {**named, **{k: v for k, v in fields.items() if v}, **({'options': options} if options else {})}
        return _call('POST', f'/jobs/{task}', body=json.dumps(body).encode(), content_type='application/json', creates=True)[0]
    body, content_type = _multipart({**fields, 'options': json.dumps(options) if options else None}, Path(source).expanduser().resolve())
    return _call('POST', f'/jobs/{task}', body=body, content_type=content_type, creates=True)[0]


def wait(job_id, timeout_seconds):
    """Wait for a job, pausing between looks for as long as the API asks (Retry-After)."""
    deadline = time.monotonic() + timeout_seconds
    shown = -1
    while True:
        job, headers = _call('GET', f'/jobs/{job_id}')
        if job['finished'] or time.monotonic() >= deadline:
            return job
        if job['progress_percent'] != shown:
            shown = job['progress_percent']
            print(f'  {job["status"].lower()} {shown}%', file=sys.stderr)
        time.sleep(max(1.0, min(float(headers.get('Retry-After') or 2), deadline - time.monotonic())))


def _free_name(directory, filename):
    """A name that is free in `directory`: a result never overwrites what is already there."""
    stem, suffix = Path(filename).stem, Path(filename).suffix
    for n in range(10000):
        candidate = directory / (filename if n == 0 else f'{stem} ({n}){suffix}')
        if not candidate.exists():
            return candidate
    raise EqualangError(f'no free name for {filename} in {directory}', 'NO_FREE_NAME')


def report(job, destination):
    """What is worth saying about a job; its files are named by where they were written."""
    summary = {
        'job_id': job['job_id'], 'task': job['task'], 'status': job['status'], 'finished': job['finished'],
        'credits_reserved': job['usage']['credits_reserved'],
        'credits_charged': job['usage']['credits_charged'] if job['finished'] else None,
    }
    if not job['finished']:
        return {**summary, 'note': f'Still running; the work continues. Pick it up with: status {job["job_id"]}'}
    if job['status'] != 'SUCCEEDED':
        problem = job.get('error') or {}
        raise EqualangError(problem.get('message') or f'the job ended as {job["status"]}', problem.get('code') or job['status'],
                            bool(problem.get('retryable')), {'job_id': job['job_id']})
    destination.mkdir(parents=True, exist_ok=True)
    outputs = []
    for output in job['outputs']:
        if not output.get('download_url'):
            raise EqualangError(f'{output["filename"]} is no longer kept', 'FILE_EXPIRED')
        path = _free_name(destination, output['filename'])
        # A signed, short-lived link: a plain GET, without the key.
        with request.urlopen(output['download_url'], timeout=300) as response:
            path.write_bytes(response.read())
        outputs.append({'kind': output['kind'], 'format': output['format'], 'path': str(path)})
    return {**summary, 'outputs': outputs}


def _destination(args, source=None):
    if args.output_dir:
        return Path(args.output_dir).expanduser().resolve()
    if source and not source.lower().startswith(('http://', 'https://')):
        return Path(source).expanduser().resolve().parent
    # A URL or an uploaded file has no "beside": the results land where the command was run.
    return Path.cwd()


def _run(task, args, **job):
    source = None if args.file_id else args.source
    if bool(args.file_id) == bool(args.source):
        raise EqualangError('Give a file (a path or URL) or --file-id, not both.', 'INVALID_SOURCE')
    created = create_job(task, source, file_id=args.file_id, **job)
    print(f'  job {created["job_id"]}: up to {created["credits_reserved"]} credits', file=sys.stderr)
    return report(wait(created['job_id'], args.timeout), _destination(args, source))


def cmd_translate(args):
    return _run('translate', args, target=args.to, source_language=args.source_language,
                options={'subtitle_bilingual': args.bilingual, 'output_formats': args.format})


def cmd_transcribe(args):
    return _run('transcribe', args, source_language=args.source_language, options={'output_formats': args.format})


def cmd_text(args):
    body = {'texts': args.texts, 'target_language': args.to, 'source_language': args.source_language}
    answer, _ = _call('POST', '/text/translate', body=json.dumps({k: v for k, v in body.items() if v}).encode(),
                      content_type='application/json', creates=True)
    return {'translations': [
        {'error': item['error']['message'], 'code': item['error']['code'], 'retryable': item['error']['retryable']} if item['error']
        else {'text': item['translated_text'], 'detected_source_language': item['detected_source_language']}
        for item in answer['translations']], 'credits_charged': answer['usage']['credits_charged']}


def cmd_estimate(args):
    body, content_type = _multipart({}, Path(args.path).expanduser().resolve())
    upload, _ = _call('POST', '/files', body=body, content_type=content_type)
    quote = upload.get('quote') or {}
    return {'file_id': upload['file_id'], 'filename': upload['filename'], 'size_bytes': upload['size_bytes'],
            'credits_to_translate': quote.get('translate'), 'credits_to_transcribe': quote.get('transcribe'),
            'kept_until': upload['expires_at']}


def cmd_status(args):
    return report(wait(args.job_id, args.wait), _destination(args))


def cmd_cancel(args):
    job, _ = _call('POST', f'/jobs/{args.job_id}/cancel')
    return {'job_id': job['job_id'], 'status': job['status'], 'finished': job['finished']}


def cmd_balance(_args):
    return _call('GET', '/credits/balance')[0]


def cmd_languages(args):
    """The languages the API takes, read from its own contract; needs no key."""
    with request.urlopen(f'{_base_url()}/openapi.json', timeout=60) as response:
        schemas = json.loads(response.read())['components']['schemas']
    choices = schemas['TextLanguage' if args.kind == 'text' else 'DocumentLanguage']['oneOf']
    wanted = (args.matching or '').lower()
    return [{'code': c['const'], 'name': c['title']} for c in choices if wanted in f'{c["const"]} {c["title"]}'.lower()]


def main(argv=None):
    parser = argparse.ArgumentParser(prog='equalang.py', description='Equalang: translate files, transcribe recordings, translate text.')
    commands = parser.add_subparsers(dest='command', required=True)

    def job_command(name, function, help_text):
        sub = commands.add_parser(name, help=help_text)
        sub.add_argument('source', nargs='?', help='a path on this machine, or a public http(s) URL (fetched by Equalang)')
        sub.add_argument('--file-id', help='a file already uploaded by `estimate`, instead of a source')
        sub.add_argument('--source-language', help='language of the file; omit to detect it')
        sub.add_argument('--format', action='append', choices=['srt', 'vtt', 'txt', 'json'], help='recordings: a format to write; repeat for several (default srt)')
        sub.add_argument('-o', '--output-dir', help='where the results go (default: beside a local source, else the current directory)')
        sub.add_argument('--timeout', type=float, default=DEFAULT_TIMEOUT_SECONDS, help='seconds to wait for the job (default %(default)s)')
        sub.set_defaults(function=function)
        return sub

    translate = job_command('translate', cmd_translate, 'translate a whole file, keeping its layout (spends credits)')
    translate.add_argument('--to', required=True, help='language to translate into, e.g. zh-CN, en, ja')
    translate.add_argument('--bilingual', action='store_true', help='subtitles and recordings: keep the original line above each translated one')
    job_command('transcribe', cmd_transcribe, 'write down what a recording says, as timed text (spends credits)')

    text = commands.add_parser('text', help='translate short plain texts (spends a little)')
    text.add_argument('texts', nargs='+', help='the texts, each translated on its own')
    text.add_argument('--to', required=True)
    text.add_argument('--source-language')
    text.set_defaults(function=cmd_text)

    estimate = commands.add_parser('estimate', help='upload a file without starting anything; prints the most a job on it can cost (free)')
    estimate.add_argument('path')
    estimate.set_defaults(function=cmd_estimate)

    status = commands.add_parser('status', help='look a job up and, if it has finished, save its results')
    status.add_argument('job_id')
    status.add_argument('--wait', type=float, default=0, help='seconds to keep waiting if it is still running (default 0)')
    status.add_argument('-o', '--output-dir')
    status.set_defaults(function=cmd_status)

    cancel = commands.add_parser('cancel', help='stop a queued or running job; a cancelled job is not charged')
    cancel.add_argument('job_id')
    cancel.set_defaults(function=cmd_cancel)

    commands.add_parser('balance', help='the account\'s credits').set_defaults(function=cmd_balance)

    languages = commands.add_parser('languages', help='the language codes, with names (no key needed)')
    languages.add_argument('matching', nargs='?', help='only those whose name or code contains this')
    languages.add_argument('--kind', choices=['file', 'text'], default='file')
    languages.set_defaults(function=cmd_languages)

    args = parser.parse_args(argv)
    try:
        print(json.dumps(args.function(args), ensure_ascii=False, indent=2))
        return 0
    except EqualangError as exc:
        print(json.dumps({'error': str(exc), 'code': exc.code or None, 'retryable': exc.retryable, **exc.data}, ensure_ascii=False, indent=2))
        return 1
    except KeyboardInterrupt:
        print('interrupted; a job already started keeps running -- `status <job_id>` picks it up', file=sys.stderr)
        return 130


if __name__ == '__main__':
    sys.exit(main())
