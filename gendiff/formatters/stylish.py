from gendiff.formatters.low import lower
import json


# def low(value):
#     if isinstance(value, str) or isinstance(value, bool):
#         return value
#     else:
#         return json.dumps(value)


def lower(value, depth=0):
    if isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    elif isinstance(value, dict):
        depth += 1
        replacer = '    ' * depth
        strings = []
        for k, v in value.items():
            strings.append(f"{replacer}{k}: {lower(v, depth + 1)}")
        return f"{{\n{'\n'.join(strings)}\n{'    ' * depth}}}"
    return str(value)


def nest(result, key, inf, replacer, depth):
    if inf.get('inside'):
        result.append(f"{replacer}    {key}: {{")
        result.append(stylish(inf['inside'], depth + 1))
        result.append(f"{replacer}    }}")
    else:
        result.append(f"{replacer}    {key}: {lower(inf['data'])}")


def stylish(value, depth=0):
    result = []
    replacer = '    ' * depth

    for key, inf in value.items():
        if inf['status'] == 'changeless':
            nest(result, key, inf, replacer, depth)
        elif inf['status'] == 'deleted':
            result.append(f"{replacer}  - {key}: {lower(inf['data'])}")
        elif inf['status'] == 'added':
            result.append(f"{replacer}  + {key}: {lower(inf['data'])}")
        elif inf['status'] == 'changed':
            result.append(f"{replacer}  - {key}: {lower(inf['data before'])}")
            result.append(f"{replacer}  + {key}: {lower(inf['data after'])}")

    return '\n'.join(result)


# ____
# def stylish(value, depth=0):
#     result = []
#     for key in value[0]:
#         if key['status'] == 'changeless':
#             if key.get('inside'):
#                 replacer = '    ' * depth
#                 result.append(f"{replacer}{key['name']}: {{")
#                 result.append(f"{replacer}{stylish(key['inside'], depth + 1)}")
#                 result.append(f"{replacer}}}")
#             else:
#                 replacer = '    ' * depth
#                 result.append(f"{replacer}{key['name']}: {lower(key['data'])}")
#         elif key['status'] == 'deleted':
#             replacer = '  - ' * depth
#             result.append(f"{replacer}{key['name']}: {lower(key['data'])}")
#         elif key['status'] == 'added':
#             replacer = '  + ' * depth
#             result.append(f"{replacer}{key['name']}: {lower(key['data'])}")
#         elif key['status'] == 'changed':
#             replacer = '  - ' * depth
#             result.append(f"{replacer}{key['name']}: {lower(key['data before'])}")
#             replacer = '  + ' * depth
#             result.append(f"{replacer}{key['name']}: {lower(key['data after'])}")
#     return '\n'.join(result)
