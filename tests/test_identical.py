from gendiff.code.opening import generate_diff
import pytest


@pytest.fixture
def file1_path():
    return 'tests/fixtures/file_identical1.json'


@pytest.fixture
def file2_path():
    return 'tests/fixtures/file_identical2.json'


def test_generate_diff(file1_path, file2_path):
    excepted = """{
    host: hexlet.io
}"""
    assert generate_diff(file1_path, file2_path) == excepted
