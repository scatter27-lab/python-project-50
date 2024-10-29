import pytest
from gendiff.code.opening import generate_diff


@pytest.fixture
def file1_path():
    return 'tests/fixtures/file_rec1.json'


@pytest.fixture
def file2_path():
    return 'tests/fixtures/file_rec2.json'


@pytest.fixture
def file1_path_yml():
    return 'tests/fixtures/file_rec1.yml'


@pytest.fixture
def file2_path_yml():
    return 'tests/fixtures/file_rec2.yml'


def test_generate_diff(file1_path, file2_path, file1_path_yml, file2_path_yml):
    excepted = """{
    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
      - setting3: true
      + setting3: null
      + setting4: blah blah
      + setting5: {
            key5: value5
        }
        setting6: {
            doge: {
              - wow: 
              + wow: so much
            }
            key: value
          + ops: vops
        }
    }
    group1: {
      - baz: bas
      + baz: bars
        foo: bar
      - nest: {
            key: value
        }
      + nest: str
    }
  - group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
  + group3: {
        deep: {
            id: {
                number: 45
            }
        }
        fee: 100500
    }
}"""
    assert generate_diff(file1_path, file2_path) == excepted
    assert generate_diff(file1_path_yml, file2_path_yml) == excepted