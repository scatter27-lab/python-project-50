#!/usr/bin/env python3
from gendiff.code.opening import generate_diff
from gendiff.gendiff_util import util


def main():
    file1, file2, format = util()
    print(generate_diff(file1, file2, format))


if __name__ == '__main__':
    main()
