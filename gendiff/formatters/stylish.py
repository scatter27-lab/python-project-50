# import json


# def stringify(value, replacer=' ', spaces_count=1):
#     def walk(value, depth):
#         indent = (str(replacer) * spaces_count) * depth
#         if type(value) == str or type(value) == bool or type(value) == int:
#             if replacer == ' ' and spaces_count == 1:
#                 return f'{str(value)}'
#             else:
#                 return f'{indent}{str(value)}'
#         if isinstance(value, dict):
#             inside = ['{']
#             keys = []
#             keys = list(value.keys())
#             for i in keys:
#                 if type(value.get(i)) != dict:
#                     inside.append(f'{indent}{i}: {value.get(i)}')
#                 if isinstance(value.get(i), dict):
#                     # рекурсия
#                     inside.append(f"{indent}{i}: {(walk(value.get(i), depth + 1))}")
#                     inside.append(f'{indent}}}')
#         if depth == 1:
#             inside.append('}')
#         return '\n'.join(inside)
#     return walk(value, 1)
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
