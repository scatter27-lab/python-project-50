import json


def stylish(file, key):
    if isinstance(file.get(key), str):
        return f'   {key}: {file.get(key)}'
    else:
        return f'   {key}: {json.dumps(file.get(key))}'
