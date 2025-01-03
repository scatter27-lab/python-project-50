import pytest
from gendiff.code.opening import generate_diff


@pytest.fixture
def file1_path():
    return 'tests/fixtures/file1.json'


@pytest.fixture
def file2_path():
    return 'tests/fixtures/file2.json'


@pytest.fixture
def file1_path_yml():
    return 'tests/fixtures/file1.yml'


@pytest.fixture
def file2_path_yml():
    return 'tests/fixtures/file2.yml'


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
