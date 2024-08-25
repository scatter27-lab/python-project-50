import json
def generate_diff(file1, file2, format=json):
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
    print(f'{{\n{'\n'.join(result)}\n}}')

generate_diff(json.load(open('../files/file1.json')),
             json.load(open('../files/file2.json')))
