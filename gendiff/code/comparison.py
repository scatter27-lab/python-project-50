import json
# from gendiff.formatters.stylish import style

def pars(file1, file2, keys):
    result = []
    for i in range(len(keys)):
        if file1.get(keys[i]) and file2.get(keys[i]):
            if file1.get(keys[i]) == file2.get(keys[i]):
                # если одинаковое
                if isinstance(file1.get(keys[i]), str):
                    result.append(f'   {keys[i]}: {file1.get(keys[i])}')
                else:
                    result.append(f'   {keys[i]}: {json.dumps(file1.get(keys[i]))}')
            else:
                # если разные value
                # result.append(f' - {keys[i]}: {file1.get(keys[i])}')
                if isinstance(file1.get(keys[i]), str):
                    result.append(f' - {keys[i]}: {file1.get(keys[i])}')
                else:
                    result.append(f' - {keys[i]}: {json.dumps(file1.get(keys[i]))}')

                if isinstance(file1.get(keys[i]), str):
                    result.append(f' + {keys[i]}: {file2.get(keys[i])}')
                else:
                    result.append(f' + {keys[i]}: {json.dumps(file2.get(keys[i]))}')

        if file1.get(keys[i]) is not None and file2.get(keys[i]) is None:
            if isinstance(file1.get(keys[i]), str):
                result.append(f' - {keys[i]}: {file1.get(keys[i])}')
            else:
                result.append(f' - {keys[i]}: {json.dumps(file1.get(keys[i]))}')

        if file1.get(keys[i]) is None and file2.get(keys[i]) is not None:
            if isinstance(file2.get(keys[i]), str):
                result.append(f' - {keys[i]}: {file2.get(keys[i])}')
            else:
                result.append(f' + {keys[i]}: {json.dumps(file2.get(keys[i]))}')

    return f'{{\n {'\n '.join(result)}\n}}'

#print(pars(json.load(open('../../tests/fixtures/file_different1.json')), json.load(open('../../tests/fixtures/file_different2.json')), ['follow']))