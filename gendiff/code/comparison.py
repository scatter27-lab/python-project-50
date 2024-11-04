import json
from gendiff.formatters.stylish import stylish


def pars(file1, file2):
    keys = list({*file1.keys(), *file2.keys()})
    keys.sort()
    prop = {}
    for i in keys:
        if i not in file1:
            prop[i] = {'status': 'added', 'data': file2[i]}
        elif i not in file2:
            prop[i] = {'status': 'deleted', 'data': file1[i]}
        elif isinstance(file1.get(i), dict) and isinstance(file2.get(i), dict):
            prop[i] = {'status': 'changeless', 'inside': pars(file1[i], file2[i])}
        elif file1.get(i) != file2.get(i):
            prop[i] = {'status': 'changed',
                       'data before': file1[i],
                       'data after': file2[i]}
        else:
            prop[i] = {'status': 'changeless', 'data': file1[i]}
    return stylish(prop)
    #return f'{{\n {'\n '.join(prop)}\n}}'
    #print(prop)
