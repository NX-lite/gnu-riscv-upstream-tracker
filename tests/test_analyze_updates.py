import json
import sys
import unittest
from dataclasses import replace
from datetime import datetime, timedelta, timezone
from pathlib import Path
from unittest.mock import Mock

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from scripts import analyze_updates as analyzer
from scripts.analyze_updates import RuleAssessment, Update, assess_update, filter_updates


def make_update(title, **changes):
    update = Update(
        repository='gcc-mirror/gcc',
        kind='commit',
        status='merged',
        sha='abc123',
        title=title,
        body='',
        author='Contributor',
        timestamp=datetime(2026, 9, 18, tzinfo=timezone.utc),
        url='https://example.test/commit/abc123',
        files=('gcc/config/riscv/riscv.cc',),
    )
    return replace(update, **changes)


def response_for(payload):
    items = json.loads(payload['messages'][1]['content'])['updates']
    return {'choices': [{'message': {'content': json.dumps({'updates': [
        {
            'id': item['id'],
            'summary_zh': '新增 RISC-V 扩展支持。',
            'impact_zh': '可能影响相关指令的生成，需要进一步验证。',
            'importance': 'high',
            'category': 'isa-extension',
            'packaging_advice_zh': '建议人工检查版本和回归测试，再决定是否打包。',
        }
        for item in items
    ]}, ensure_ascii=False)}}]}


class ConfigTests(unittest.TestCase):
    def test_config_lists_the_mirrors_we_scan(self):
        config = json.loads((PROJECT_ROOT / 'config/repos.json').read_text(encoding='utf-8'))

        self.assertEqual(config['default_lookback_days'], 7)
        self.assertEqual(
            [(entry['repo'], entry['branch']) for entry in config['repositories']],
            [
                ('gcc-mirror/gcc', 'master'),
                ('RTEMS/sourceware-mirror-binutils-gdb', 'master'),
                ('sailfishos-mirror/glibc', 'master'),
            ],
        )
        rules = config['rules']
        self.assertTrue(rules['riscv_tokens'])
        for category in ('hardware', 'isa-extension', 'profile-abi', 'compiler-option',
                         'vector-crypto-hypervisor', 'bugfix'):
            self.assertTrue(rules['category_keywords'][category])


class RuleTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rules = json.loads((PROJECT_ROOT / 'config/repos.json').read_text(encoding='utf-8'))['rules']

    def test_riscv_relevance_needs_a_path_or_a_token(self):
        self.assertIsNotNone(assess_update(make_update('Fix codegen'), self.rules))
        self.assertIsNone(assess_update(
            make_update('Add AVX512 support', files=('gcc/config/i386/i386.cc',)), self.rules))
        for title in ('RISC-V: Add vector support', 'RISCV: Add vector support', 'rv64gc: Add vector support'):
            with self.subTest(title=title):
                result = assess_update(make_update(title, files=()), self.rules)
                self.assertEqual(result.importance, 'high')
                self.assertTrue(any(rule.startswith('token:') for rule in result.matched_rules))

    def test_new_support_is_high_and_explains_itself(self):
        cases = [
            ('Add SpacemiT K3 support', 'hardware'),
            ('Add Zba extension support', 'isa-extension'),
            ('Support lp64 ABI', 'profile-abi'),
            ('Add -march parsing option', 'compiler-option'),
        ]
        for title, category in cases:
            with self.subTest(title=title):
                result = assess_update(make_update(title), self.rules)
                self.assertEqual((result.category, result.importance), (category, 'high'))
                self.assertTrue(result.packaging_candidate)
                self.assertTrue(any(rule.startswith('keyword:' + category) for rule in result.matched_rules))

    def test_bugfixes_stay_medium(self):
        for title in ('RISC-V: Fix Zba extension wrong-code', 'RISC-V: Fix vector regression',
                      'RISC-V: Correct ABI handling'):
            with self.subTest(title=title):
                result = assess_update(make_update(title), self.rules)
                self.assertEqual((result.category, result.importance), ('bugfix', 'medium'))

    def test_cleanup_and_test_only_changes_are_low(self):
        cases = [
            make_update('RISC-V: Clean up Zba extension support'),
            make_update('RISC-V: Fix comments describing vector support'),
            make_update('RISC-V: Correct typo in ABI documentation'),
            make_update('RISC-V: Reformat vector code'),
            make_update('RISC-V: Add Zce extension support',
                        files=('gcc/testsuite/gcc.target/riscv/zce.c', 'gcc/ChangeLog')),
        ]
        for update in cases:
            with self.subTest(title=update.title, files=update.files):
                result = assess_update(update, self.rules)
                self.assertEqual((result.category, result.importance), ('other', 'low'))
                self.assertFalse(result.packaging_candidate)

    def test_tests_alongside_a_feature_are_not_cleanup(self):
        for title in ('RISC-V: Add Zba support and tests', 'RISC-V: Add Zba support with tests'):
            with self.subTest(title=title):
                result = assess_update(make_update(title), self.rules)
                self.assertEqual((result.category, result.importance), ('isa-extension', 'high'))

    def test_generic_words_do_not_raise_priority(self):
        result = assess_update(make_update('RISC-V: Update target handling'), self.rules)
        self.assertNotEqual(result.importance, 'high')

    def test_body_text_can_establish_relevance(self):
        result = assess_update(
            make_update('Implement new extension', body='Add RISC-V Zba support', files=()), self.rules)
        self.assertEqual((result.category, result.importance), ('isa-extension', 'high'))

    def test_filter_order_is_stable(self):
        older = make_update('RISC-V: Add Zba support', sha='a')
        newer = replace(older, sha='b', timestamp=older.timestamp + timedelta(days=1))
        fix = make_update('RISC-V: Fix regression', sha='c')
        low = make_update('RISC-V: Fix comments', sha='d')
        excluded = make_update('x86: Add support', files=(), sha='e')
        updates = [low, older, excluded, fix, newer]

        expected = ['b', 'a', 'c', 'd']
        self.assertEqual([item.sha for item, _ in filter_updates(updates, self.rules)], expected)
        self.assertEqual([item.sha for item, _ in filter_updates(reversed(updates), self.rules)], expected)

    def test_rule_evidence_is_sorted_and_deduplicated(self):
        assessment = RuleAssessment('compiler-option', 'high',
                                    ('riscv-token', 'compiler-keyword', 'riscv-token'), True)
        self.assertEqual(assessment.to_dict()['matched_rules'], ['compiler-keyword', 'riscv-token'])


class AnalysisTests(unittest.TestCase):
    def setUp(self):
        self.update = make_update('RISC-V: Add Zba support', body='Metadata only')
        self.rules = RuleAssessment('isa-extension', 'high', ('path:riscv', 'keyword:isa-extension:zba'), True)
        self.assessed = [(self.update, self.rules)]
        self.prompt = (PROJECT_ROOT / 'prompts/analyze-updates.md').read_text(encoding='utf-8')

    def analyze(self, post_json, assessed=None, api_key='test-secret'):
        return analyzer.analyze_updates(
            self.assessed if assessed is None else assessed,
            api_key=api_key,
            prompt=self.prompt,
            post_json=post_json,
        )

    def test_successful_call_sends_expected_request(self):
        requests = []

        def post_json(url, headers, payload):
            requests.append((url, headers, payload))
            return response_for(payload)

        result = self.analyze(post_json)

        self.assertEqual(result[0].analysis_mode, 'llm')
        self.assertIs(result[0].update, self.update)
        self.assertIs(result[0].rules, self.rules)
        self.assertEqual(result[0].llm_assessment, {'importance': 'high', 'category': 'isa-extension'})
        self.assertIsNone(result[0].analysis_warning)

        url, headers, payload = requests[0]
        self.assertEqual(url, analyzer.API_URL)
        self.assertEqual(headers['Authorization'], 'Bearer test-secret')
        self.assertEqual(payload['model'], analyzer.MODEL)
        self.assertEqual(payload['messages'][0]['content'], self.prompt)
        self.assertNotIn('test-secret', json.dumps(payload))

    def test_model_advice_never_overrides_the_rules(self):
        def post_json(url, headers, payload):
            response = response_for(payload)
            content = json.loads(response['choices'][0]['message']['content'])
            content['updates'][0].update({'importance': 'low', 'category': 'other'})
            response['choices'][0]['message']['content'] = json.dumps(content)
            return response

        result = self.analyze(post_json)[0]

        self.assertEqual(result.llm_assessment, {'importance': 'low', 'category': 'other'})
        self.assertEqual((result.rules.importance, result.rules.category), ('high', 'isa-extension'))

    def test_without_a_key_nothing_is_sent(self):
        def unexpected(*args):
            self.fail('没有密钥时不应该发请求')

        for api_key in (None, '', '   '):
            with self.subTest(api_key=api_key):
                result = self.analyze(unexpected, api_key=api_key)
                self.assertEqual(result[0].analysis_mode, 'rules-only')
                self.assertIn('LLM_API_KEY', result[0].analysis_warning)
        self.assertEqual(self.analyze(unexpected, assessed=[]), [])

    def test_url_and_model_are_restricted_to_the_allowlist(self):
        for url in ('https://api.deepseek.com/chat/completions',
                    'https://api.deepseek.com/v1/chat/completions'):
            with self.subTest(url=url):
                transport = Mock(side_effect=lambda url, headers, payload: response_for(payload))
                result = analyzer.analyze_updates(self.assessed, api_key='test-secret', prompt=self.prompt,
                                                  api_url=url, model='deepseek-v4-pro', post_json=transport)
                self.assertEqual(result[0].analysis_mode, 'llm')
                self.assertEqual(transport.call_args.args[2]['model'], 'deepseek-v4-pro')

        rejected = [
            {'api_url': 'http://api.deepseek.com/chat/completions'},
            {'api_url': 'https://other.example.test/chat/completions'},
            {'api_url': 'https://api.deepseek.com.other.example.test/chat/completions'},
            {'api_url': 'https://test-secret@api.deepseek.com/chat/completions'},
            {'api_url': 'https://api.deepseek.com/chat/completions?key=test-secret'},
            {'model': 'deepseek/chat'},
            {'model': 'x' * 101},
        ]
        for setting in rejected:
            with self.subTest(setting=setting):
                transport = Mock()
                result = analyzer.analyze_updates(self.assessed, api_key='test-secret', prompt=self.prompt,
                                                  post_json=transport, **setting)
                transport.assert_not_called()
                self.assertEqual(result[0].analysis_mode, 'rules-only')
                self.assertIn('配置无效', result[0].analysis_warning)

    def test_blank_provider_settings_fall_back_to_defaults(self):
        for value in (None, '', '   '):
            with self.subTest(value=value):
                transport = Mock(side_effect=lambda url, headers, payload: response_for(payload))
                analyzer.analyze_updates(self.assessed, api_key='test-secret', prompt=self.prompt,
                                         api_url=value, model=value, post_json=transport)
                self.assertEqual(transport.call_args.args[0], analyzer.API_URL)
                self.assertEqual(transport.call_args.args[2]['model'], analyzer.MODEL)

    def test_unusable_responses_fall_back_to_rules(self):
        def mutate(field, value):
            def post_json(url, headers, payload):
                response = response_for(payload)
                content = json.loads(response['choices'][0]['message']['content'])
                content['updates'][0][field] = value
                response['choices'][0]['message']['content'] = json.dumps(content)
                return response
            return post_json

        cases = [
            {},
            {'choices': []},
            {'choices': [{'message': {'content': 'not JSON'}}]},
            {'choices': [{'message': {'content': '```json\n{"updates": []}\n```'}}]},
            {'choices': [{'message': {'content': '{"updates": []}'}}]},
            mutate('importance', 'critical'),
            mutate('category', 'compiler'),
            mutate('summary_zh', ''),
            mutate('summary_zh', 'English only'),
            mutate('impact_zh', '中' * 2000),
            mutate('status', 'released'),
        ]
        for response in cases:
            with self.subTest(response=str(response)[:40]):
                transport = response if callable(response) else (lambda *args: response)
                result = self.analyze(transport)[0]
                self.assertEqual(result.analysis_mode, 'rules-only')
                self.assertEqual(result.analysis_warning, 'LLM 请求失败或响应无效，使用规则结果。')

    def test_repeated_ids_or_missing_updates_reject_the_batch(self):
        assessed = self.assessed + [(replace(self.update, sha='other'), self.rules)]
        for mode in ('duplicate', 'unknown', 'missing'):

            def post_json(url, headers, payload, mode=mode):
                response = response_for(payload)
                content = json.loads(response['choices'][0]['message']['content'])
                if mode == 'duplicate':
                    content['updates'][1]['id'] = content['updates'][0]['id']
                elif mode == 'unknown':
                    content['updates'][1]['id'] = 'unknown'
                else:
                    content['updates'].pop()
                response['choices'][0]['message']['content'] = json.dumps(content)
                return response

            result = self.analyze(post_json, assessed=assessed)
            self.assertTrue(all(item.analysis_mode == 'rules-only' for item in result))

    def test_key_echoed_in_the_response_invalidates_it(self):
        for field in ('summary_zh', 'impact_zh', 'packaging_advice_zh'):
            with self.subTest(field=field):
                def post_json(url, headers, payload):
                    response = response_for(payload)
                    content = json.loads(response['choices'][0]['message']['content'])
                    content['updates'][0][field] = '敏感内容 test-secret'
                    response['choices'][0]['message']['content'] = json.dumps(content).replace(
                        'test-secret', '\\u0074est-secret')
                    return response

                result = self.analyze(post_json)[0]

                self.assertEqual(result.analysis_mode, 'rules-only')
                self.assertNotIn('test-secret', json.dumps(result.to_dict()))

    def test_timeout_warning_does_not_repeat_the_exception(self):
        def timeout(*args):
            raise TimeoutError('Authorization: Bearer test-secret; private response')

        result = self.analyze(timeout)[0]

        self.assertEqual(result.analysis_warning, 'LLM 请求超时，使用规则结果。')
        self.assertNotIn('test-secret', json.dumps(result.to_dict()))
        self.assertNotIn('private response', json.dumps(result.to_dict()))

    def test_one_failed_batch_does_not_discard_the_others(self):
        assessed = [(replace(self.update, sha=str(index)), self.rules)
                    for index in range(analyzer.BATCH_SIZE + 1)]
        requests = []

        def post_json(url, headers, payload):
            requests.append(payload)
            if len(requests) == 1:
                raise TimeoutError('failure')
            return response_for(payload)

        result = self.analyze(post_json, assessed=assessed)

        self.assertEqual(len(requests), 2)
        self.assertTrue(all(item.analysis_mode == 'rules-only' for item in result[:-1]))
        self.assertEqual(result[-1].analysis_mode, 'llm')

    def test_batch_limits_cap_the_calls_without_losing_updates(self):
        update = replace(self.update, body='中' * 100000, files=tuple('中' * 1000 for _ in range(100)))
        count = analyzer.BATCH_SIZE * analyzer.MAX_BATCHES + 3
        assessed = [(replace(update, sha=str(index)), self.rules) for index in range(count)]
        requests = []

        def post_json(url, headers, payload):
            requests.append(payload)
            size = len(json.dumps(payload, ensure_ascii=False).encode())
            self.assertLessEqual(size, analyzer.MAX_REQUEST_BYTES)
            self.assertLessEqual(len(json.loads(payload['messages'][1]['content'])['updates']),
                                 analyzer.BATCH_SIZE)
            return response_for(payload)

        result = self.analyze(post_json, assessed=assessed)

        self.assertEqual(len(result), count)
        self.assertLessEqual(len(requests), analyzer.MAX_BATCHES)
        self.assertEqual(result[-1].analysis_mode, 'rules-only')

    def test_oversize_response_is_rejected(self):
        response = {'choices': [{'message': {'content': '中' * analyzer.MAX_RESPONSE_BYTES}}]}
        self.assertEqual(self.analyze(lambda *args: response)[0].analysis_mode, 'rules-only')


if __name__ == '__main__':
    unittest.main()
