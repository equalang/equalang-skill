"""Exercise CLI parsing and HTTP serialization without spending credits."""

import contextlib
import io
import json
import tempfile
import unittest
from email import policy
from email.parser import BytesParser
from pathlib import Path
from unittest.mock import patch

from scripts import equalang


class DocumentOptionsTest(unittest.TestCase):
    def test_formula_option_reaches_every_input_transport(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'report.pdf'
            path.write_bytes(b'%PDF-1.7\n')
            sources = [[str(path)], ['https://example.com/report.pdf'], ['--file-id', 'uploaded-file']]
            variants = [([], None), (['--optimize-math-formula'], True), (['--no-optimize-math-formula'], False)]
            for source in sources:
                for flags, enabled in variants:
                    with self.subTest(source=source, enabled=enabled):
                        sent = []

                        def respond(req, **kwargs):
                            if req.get_method() == 'POST':
                                sent.append(req)
                                data = {'job_id': 'test-job', 'credits_reserved': 1}
                            else:
                                data = {'job_id': 'test-job', 'task': 'translate', 'status': 'RUNNING',
                                        'finished': False, 'usage': {'credits_reserved': 1}}
                            response = io.BytesIO(json.dumps({'data': data}).encode())
                            response.headers = {}
                            return response

                        with patch.object(equalang, '_setting', side_effect=lambda key: {
                            'EQUALANG_API_KEY': 'el_test_only', 'EQUALANG_BASE_URL': 'https://api.example/v1',
                        }.get(key, '')), patch.object(equalang.request, 'urlopen', side_effect=respond), \
                                contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
                            self.assertEqual(equalang.main(['translate', *source, '--to', 'uk', '--timeout', '0', *flags]), 0)
                        self.assertEqual(len(sent), 1)
                        req = sent[0]
                        self.assertEqual(req.full_url, 'https://api.example/v1/jobs/translate')
                        content_type = req.get_header('Content-type')
                        if content_type.startswith('multipart/'):
                            message = BytesParser(policy=policy.default).parsebytes(
                                f'Content-Type: {content_type}\r\n\r\n'.encode() + req.data)
                            fields = {part.get_param('name', header='content-disposition'):
                                      part.get_payload(decode=True).decode() for part in message.iter_parts()}
                            self.assertEqual(fields['file'], '%PDF-1.7\n')
                            options = json.loads(fields.get('options', '{}'))
                        else:
                            fields = json.loads(req.data)
                            options = fields.get('options', {})
                            self.assertEqual(fields.get('file_url') or fields.get('file_id'), source[-1])
                        self.assertEqual(fields['target_language'], 'uk')
                        self.assertEqual(options, {} if enabled is None else {'optimize_math_formula': enabled})

    def test_incompatible_flags_are_rejected_before_http(self):
        for args in [
            ['translate', 'a.pdf', '--to', 'uk', '--optimize-math-formula', '--no-optimize-math-formula'],
            ['transcribe', 'a.mp3', '--optimize-math-formula'],
        ]:
            with self.subTest(args=args), patch.object(equalang.request, 'urlopen') as http, \
                    contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit) as error:
                equalang.main(args)
            self.assertEqual(error.exception.code, 2)
            http.assert_not_called()

    def test_languages_follow_the_deployments_catalog(self):
        catalog = {'components': {'schemas': {
            'DocumentLanguage': {'oneOf': [{'const': 'uk', 'title': 'Ukrainian'}]},
            'TextLanguage': {'oneOf': [{'const': 'en', 'title': 'English'}]},
        }}}
        for kind, expected in [('file', 'uk'), ('text', 'en')]:
            output = io.StringIO()
            with patch.object(equalang.request, 'urlopen', return_value=io.BytesIO(json.dumps(catalog).encode())), \
                    contextlib.redirect_stdout(output):
                self.assertEqual(equalang.main(['languages', '--kind', kind]), 0)
            self.assertEqual([item['code'] for item in json.loads(output.getvalue())], [expected])


if __name__ == '__main__':
    unittest.main()
