import json
from gendiff.formatters.stylish import stylish
from gendiff.code.opening import generate_diff

# def pars(file1, file2, keys):
#     result = []
#     position = {}
#     for i in range(len(keys)):
#         position["key"] = keys[i]
#         if file1.get(keys[i]):
#             position["file1"] = file1.get(keys[i])
#         if file2.get(keys[i]):
#             position["file2"] = file2.get(keys[i])
#
#         if position.get('file1') == position.get('file2'):
#             position["difference"] = 'identical'
#             result.append(stylish(position))
#         if position.get('file2') is None and
#         position.get('file1') is not None:
#             position["difference"] = 'only_one'
#             result.append(stylish(position))
#         if position.get('file1') is None and
#         position.get('file2') is not None:
#             position["difference"] = 'only_second'
#             result.append(stylish(position))
#         if (position.get('file2') and position.get('file1'))
#         is not None and (position.get('file1')
#         != position.get('file2')):
#             position["difference"] = 'differ'
#             result.append(stylish(position))

# if file1.get(keys[i]) is not None and file2.get(keys[i]) is None:
#     if isinstance(file1.get(keys[i]), str):
#         result.append(f' - {keys[i]}: {file1.get(keys[i])}')
#     else:
#         result.append(f' - {keys[i]}: {json.dumps(file1.get(keys[i]))}')
#
# if file1.get(keys[i]) is None and file2.get(keys[i]) is not None:
#     if isinstance(file2.get(keys[i]), str):
#         result.append(f' + {keys[i]}: {file2.get(keys[i])}')
#     else:
#         result.append(f' + {keys[i]}: {json.dumps(file2.get(keys[i]))}')
#
# return f'{{\n {'\n '.join(result)}\n}}'
# ________________________________________________________________________________
# print(pars(json.load(open('../../tests/fixtures/file_different1.json')),
# json.load(open('../../tests/fixtures/file_different2.json')), ['follow']))
def pars(file1, file2):
    keys = list({*file1.keys(), *file2.keys()})
    keys.sort()
    prop = []
    for i in keys:
        value = {'name': i}
        if i not in file1:
            value['status'] = 'added'
            value['data'] = file2[i]
        elif i not in file2:
            value['status'] = 'deleted'
            value['data'] = file1[i]
        elif isinstance(file1.get(i), dict) and isinstance(file2.get(i), dict):
            value['status'] = 'nest'
            value['inside'] = pars(file1.get(i), file2.get(i))
        elif file1.get(i) == file2.get(i):
            value['status'] = 'changeless'
            value['data'] = file1[i]
        else:
            value['status'] = 'changed'
            value['data before'] = file1[i]
            value['data after'] = file2[i]
        prop.append(value)
    return stylish(prop)
    #return f'{{\n {'\n '.join(prop)}\n}}'
