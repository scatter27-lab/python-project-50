from gendiff.code.opening import generate_diff

assert (generate_diff('tests/fixtures/file_different1.json',
                      'tests/fixtures/file_different2.json')
        == f'{{\n  + follow: False\n  - proxy: 123.234.53.22\n}}')
assert (generate_diff('tests/fixtures/file_different1.yml',
                      'tests/fixtures/file_different2.yml')
        == f'{{\n  + follow: False\n  - proxy: 123.234.53.22\n}}')
assert (generate_diff('tests/fixtures/file_different1.yaml',
                      'tests/fixtures/file_different2.yaml') 
        == f'{{\n  + follow: False\n  - proxy: 123.234.53.22\n}}')