import json
def generate_diff(file1, file2, format=json):
    file1 = json.load(open(file1))
    file2 = json.load(open(file2))
    result = []
    keys = list({*file1.keys(), *file2.keys()})
    keys.sort()

    for i in range(len(keys)):
        if file1.get(keys[i]) and file2.get(keys[i]):
            if file1.get(keys[i]) == file2.get(keys[i]):
                result.append(f'   {keys[i]}: {file1.get(keys[i])}')  # если одинаковое
            else:
                result.append(f' - {keys[i]}: {file1.get(keys[i])}')  #  если разные value
                result.append(f' + {keys[i]}: {file2.get(keys[i])}')

        if file1.get(keys[i]) is not None and file2.get(keys[i]) is None:
            result.append(f' - {keys[i]}: {file1.get(keys[i])}')

        if file1.get(keys[i]) is None and file2.get(keys[i]) is not None:
            result.append(f' + {keys[i]}: {file2.get(keys[i])}')
    return f'{{\n {'\n '.join(result)}\n}}'

#print(generate_diff('../../tests/fixtures/file_different1.json','../../tests/fixtures/file_different2.json'))
