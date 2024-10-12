from gendiff.code.opening import generate_diff


# assert (generate_diff('fixtures/file1.json','fixtures/file2.json')
# == f'{{\n - follow: False\n   host: hexlet.io\n -
# proxy: 123.234.53.22\n - timeout: 50\n +
# timeout: 20\n + verbose: True \n}}')
file1 = 'fixtures/file_identical1.json'
file2 = 'fixtures/file_identical2.json'
assert generate_diff(file1, file2) == "{\n    host: hexlet.io\n}"
