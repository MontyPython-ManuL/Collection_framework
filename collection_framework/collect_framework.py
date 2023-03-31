from collections import Counter
from functools import lru_cache
import functools
import argparse


@lru_cache(maxsize=32)
def count_unique_char(text):
    return len([i for i in Counter(text).values() if i == 1])


def create_parser_with_arguments():
    parser = argparse.ArgumentParser(description='The program counts the number of unique characters in a string or '
                                                 'file that was passed as an input argument')
    parser.add_argument('--string', type=str, help='Input string for counts the number of unique characters')
    parser.add_argument('--file', type=get_string, help='Input file path for read and '
                                                        'counts the number of unique characters')
    return parser


def get_parse_data(parser):
    data = parser.parse_known_args()[0]
    return data.string, data.file


def get_string(filename):
    if not filename:
        return None
    with open(filename, 'r') as file:
        return file.read()


def main():
    parser = create_parser_with_arguments()
    parsed_string, parsed_file = get_parse_data(parser)
    finally_string = parsed_file or parsed_string
    print(count_unique_char(finally_string))


if __name__ == '__main__':
    main()
