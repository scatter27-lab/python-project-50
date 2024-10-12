import pytest
from gendiff.code.opening import generate_diff


@pytest.fixture
def file1_path():
    return 'fixtures/file1.json'


@pytest.fixture
def file2_path():
    return 'fixtures/file2.json'


def test_generate_diff(file1_path, file2_path):
    excepted = """{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""
    assert generate_diff(file1_path, file2_path) == excepted

# assert (generate_diff('fixtures/file_different1.yml',
#                       'fixtures/file_different2.yml')
#         == f'{{\n  + follow: false\n  - proxy: 123.234.53.22\n}}')
# assert (generate_diff('fixtures/file_different1.yaml',
#                       'fixtures/file_different2.yaml')
#         == f'{{\n  + follow: false\n  - proxy: 123.234.53.22\n}}')
