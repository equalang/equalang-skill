#!/usr/bin/env python3
"""Check this skill against the API it talks to.

A published skill rots when the API moves, in someone else's install. This
reads the API's public contract and verifies that every path equalang.py
builds, and every field it reads, is one the contract still documents.
No credentials: anyone who forks this can run it.

    python3 scripts/check_api.py
    EQUALANG_BASE_URL=https://test.equalang.com/v1 python3 scripts/check_api.py
"""

import json
import os
import re
import sys
from pathlib import Path
from urllib import request

BASE_URL = (os.environ.get('EQUALANG_BASE_URL') or 'https://equalang.com/v1').rstrip('/')
SOURCE = (Path(__file__).parent / 'equalang.py').read_text(encoding='utf-8')
FIELDS = {
    'File': ['file_id', 'filename', 'size_bytes', 'expires_at', 'quote'],
    'Job': ['job_id', 'task', 'status', 'finished', 'progress_percent', 'outputs', 'error', 'usage'],
    'JobOutput': ['kind', 'format', 'filename', 'download_url'],
    'JobUsage': ['credits_reserved', 'credits_charged'],
    'ErrorResponse': ['code', 'message', 'retryable'],
    'DocumentTranslateOptions': ['subtitle_bilingual', 'output_formats'],
}


def main():
    with request.urlopen(f'{BASE_URL}/openapi.json', timeout=60) as response:
        document = json.loads(response.read())
    print(f'contract {document["info"]["version"]} at {BASE_URL}')
    known = [re.sub(r'\{[^}]+\}', 'x', path) for path in document['paths']]
    failures = 0
    for written in sorted(set(re.findall(r"'(/(?:jobs|files|text|credits)[^']*)'", SOURCE))):
        shape = re.compile('^' + re.sub(r'\{[^}]+\}', '[^/]+', written) + '$')
        ok = any(shape.match(path) for path in known)
        failures += not ok
        print(f'  [{"OK " if ok else "FAIL"}] {written} is a documented path')
    schemas = document['components']['schemas']
    for schema, fields in FIELDS.items():
        missing = [field for field in fields if field not in schemas.get(schema, {}).get('properties', {})]
        failures += bool(missing)
        print(f'  [{"OK " if not missing else "FAIL"}] {schema} still has {", ".join(fields)}' + (f' - missing {missing}' if missing else ''))
    # What SKILL.md promises an agent is checked too: a format the API dropped would be a lie told on every load.
    root = Path(__file__).parent.parent
    formats = re.search(r'\*\*Formats\.\*\*(.*)', (root / 'SKILL.md').read_text(encoding='utf-8')).group(1)
    promised = set(re.findall(r'\b[a-z0-9]{2,5}\b(?=[,.])', formats.split('Up to')[0]))
    accepted = set(schemas['File']['properties']['extension']['enum'])
    wrong = sorted(promised - accepted) + sorted(accepted - promised - {'jpeg'})
    failures += bool(wrong)
    print(f'  [{"OK " if not wrong else "FAIL"}] SKILL.md names exactly the formats the API accepts' + (f' - {wrong}' if wrong else ''))
    request_schema = schemas['PublicTextTranslateRequest']['properties']
    skill = (root / 'SKILL.md').read_text(encoding='utf-8')
    limits = (f"at most {request_schema['texts']['maxItems']} of {request_schema['texts']['items']['maxLength']:,} characters, "
              f"{request_schema['texts']['x-max-total-characters']:,} per call", f"up to {request_schema.get('text', {}).get('maxLength', 0):,} characters")
    stated = all(limit in skill for limit in limits)
    failures += not stated
    print(f'  [{"OK " if stated else "FAIL"}] SKILL.md states the text limits the API enforces')
    version = re.search(r"^VERSION = '([^']+)'", SOURCE, re.M).group(1)
    manifests = [json.loads((root / '.claude-plugin' / name).read_text()) for name in ('plugin.json', 'marketplace.json')]
    same = manifests[0]['version'] == version and manifests[1]['plugins'][0]['version'] == version
    failures += not same
    print(f'  [{"OK " if same else "FAIL"}] the script and both manifests name version {version}')
    print(f'{failures} FAILURES' if failures else 'The skill matches the contract.')
    return 1 if failures else 0


if __name__ == '__main__':
    sys.exit(main())
