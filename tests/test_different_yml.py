import pytest
from gendiff.code.opening import generate_diff


@pytest.fixture
def file1_path():
    return 'tests/fixtures/file1.yml'


@pytest.fixture
def file2_path():
    return 'tests/fixtures/file2.yml'


@pytest.fixture
def file1_path_yaml():
    return 'tests/fixtures/file1.yaml'


@pytest.fixture
def file2_path_yaml():
    return 'tests/fixtures/file2.yaml'


def test_generate_diff(file1_path, file2_path, file1_path_yaml, file2_path_yaml):
    excepted = """{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""
    assert generate_diff(file1_path, file2_path) == excepted
    assert generate_diff(file1_path_yaml, file2_path_yaml) == excepted