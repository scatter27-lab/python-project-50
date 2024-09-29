#!/usr/bin/env python3
import argparse
from gendiff.code.opening import generate_diff


def main():
    parser = argparse.ArgumentParser(prog="gendiff",
                                     description="Compares "
                                                 "two configuration files "
                                                 "and shows a difference.")
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument("-f", "--format", help="set format of output")
    args = parser.parse_args()
    different = generate_diff(args.first_file, args.second_file, args.format)
    print(different)


if __name__ == '__main__':
    main()
