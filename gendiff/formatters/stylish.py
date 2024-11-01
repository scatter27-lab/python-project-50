import json


def stylish(value, replacer='   ', spaces_count=1):

    def walk(value, depth=0):
        result = []
        for key in value:
            if key['status'] == 'changeless':
                replacer = '    '
                result.append(f"{replacer}{key['name']}: {key['data']}")
            if key['status'] == 'deleted':
                replacer = '  - '
                result.append(f"{replacer}{key['name']}: {key['data']}")
            if key['status'] == 'added':
                replacer = '  + '
                result.append(f"{replacer}{key['name']}: {key['data']}")
            if key['status'] == 'changed':
                replacer = '  - '
                result.append(f"{replacer}{key['name']}: {key['data before']}")
                replacer = '  + '
                result.append(f"{replacer}{key['name']}: {key['data after']}")
            if key['status'] == 'nest':
                result.append(walk(key, depth + 1))
        result.append('}')
        return '\n'.join(result)

    return walk(value, 1)
# _______________________________________
# def stylish(position):
#     style = ''
#     if position["difference"] == 'identical':
#         if isinstance(position.get('file1'), str):
#             return f'   {position['key']}: {position['file1']}'
#         else:
#             return f'   {position['key']}:
#             {json.dumps(position.get('file1'))}'
#
#     if position["difference"] == 'only_one':
#         if isinstance(position.get('file1'), str):
#             style += f' - {position['key']}: {position['file1']}\n'
#         else:
#             style += f' - {position['key']}: {json.dumps(position['file1'])}'
#     if position["difference"] == 'only_second':
#         if isinstance(position.get('file2'), str):
#             style += f' + {position['key']}: {position['file2']}\n'
#         else:
#             style += f' + {position['key']}: {json.dumps(position['file2'])}'
#     if position["difference"] == 'differ':
#         if isinstance(position.get('file1'), str):
#             style += f' - {position['key']}: {position['file1']}\n'
#         else:
#             style += f' - {position['key']}: {json.dumps(position['file1'])}'
#         if isinstance(position.get('file2'), str):
#             style += f' + {position['key']}: {position['file2']}'
#         else:
#             style += f' + {position['key']}: {json.dumps(position['file2'])}'
#     return style

# if isinstance(position.get('file2'), str):
#     return f'{style} {{/n + {position['key']}: {position['file2']}'
# else:
#     return (f'{style} {{/n + {position['key']}: '
#             f'{json.dumps(position['file2'])}')
