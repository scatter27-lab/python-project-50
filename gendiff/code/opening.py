import json
import yaml
from yaml import SafeLoader
from gendiff.code.comparison import pars
from gendiff.formatters.stylish import stylish


def generate_diff(file1, file2, format_name='stylish'):
    if file1.endswith('.json'):
        file1 = json.load(open(file1))
    elif file1.endswith(('.yaml', '.yml')):
        file1 = yaml.load(open(file1), Loader=SafeLoader)
    if file2.endswith('.json'):
        file2 = json.load(open(file2))
    elif file2.endswith(('.yaml', '.yml')):
        file2 = yaml.load(open(file2), Loader=SafeLoader)
    diff = pars(file1, file2)
    return f"{{\n{stylish(diff)}\n}}"

