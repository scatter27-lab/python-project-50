import difficult_calculator
from difficult_calculator.code.compare import generate_diff

assert (generate_diff('tests/fixtures/file_different1.json','tests/fixtures/file_different2.json') ==
        f'{{\n + follow: False\n - proxy: 123.234.53.22\n}}')
