#!/usr/bin/env python3
from pprint import pprint
import os
import sys

def pretty_print_dict():
    my_vars = {} 
    for item, value in os.environ.items():
        my_vars[item] = value
    pprint(my_vars, width=1)

def print_like_gnu_env():
    for item, value in os.environ.items():
        print(f'{item}={value}')
def main():
    if len(sys.argv) == 1:
        return pretty_print_dict()
    else:
        option = sys.argv[1]
        if option == 'clean':
            print_like_gnu_env()


if __name__ == '__main__':
    main()


