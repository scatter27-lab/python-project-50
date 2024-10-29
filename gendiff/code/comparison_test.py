import json
# from gendiff.formatters.stylish import stylish


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
def pars(file1, file2, keys):
    result = []
    position = {}
    for i in range(len(keys)):
        position["key"] = keys[i]
        if file1.get(keys[i]):
            position["file1"] = file1.get(keys[i])
        if file1.get(keys[i]):
            position["file2"] = file2.get(keys[i])
        if file1.get(keys[i]) and file2.get(keys[i]):
            if file1.get(keys[i]) == file2.get(keys[i]):
                # если одинаковое
                # result.append(stylish(file1, keys[i]))
                result.append(f'   {keys[i]}: {file1.get(keys[i])}')
            else:
                # если разные value
                # result.append(f' - {keys[i]}: {file1.get(keys[i])}')
                if isinstance(file1.get(keys[i]), str):
                    result.append(f' - {keys[i]}: {file1.get(keys[i])}')
                else:
                    result.append(f' - {keys[i]}: '
                                  f'{json.dumps(file1.get(keys[i]))}')

                if isinstance(file1.get(keys[i]), str):
                    result.append(f' + {keys[i]}: {file2.get(keys[i])}')
                else:
                    result.append(f' + {keys[i]}: '
                                  f'{json.dumps(file2.get(keys[i]))}')

        if file1.get(keys[i]) is not None and file2.get(keys[i]) is None:
            if isinstance(file1.get(keys[i]), str):
                result.append(f' - {keys[i]}: {file1.get(keys[i])}')
            else:
                result.append(f' - {keys[i]}: {json.dumps(file1.get(keys[i]))}')

        if file1.get(keys[i]) is None and file2.get(keys[i]) is not None:
            if isinstance(file2.get(keys[i]), str):
                result.append(f' + {keys[i]}: {file2.get(keys[i])}')
            else:
                result.append(f' + {keys[i]}: {json.dumps(file2.get(keys[i]))}')

    return f'{{\n {'\n '.join(result)}\n}}'