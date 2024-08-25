#!/usr/bin/env python3
import argparse
import json

def generate_diff(file1: str, file2: str, format='json'):
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
    return f'{{\n{'\n'.join(result)}\n}}'


def main():
    parser = argparse.ArgumentParser(prog="gendiff",
        description="Compares two configuration files and shows a difference.")
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument("-f", "--format", help="set format of output")
    args = parser.parse_args()
    print(generate_diff(args.first_file, args.second_file))

if __name__ == '__main__':
    main()