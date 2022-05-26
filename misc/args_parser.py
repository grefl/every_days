#!/bin/env python3
import sys

SUPPORTED_ARGS = ['--time-from', '--time-to']

def check_args_or_fail(args_split):
    if any(True if arg not in args_split else False for arg in SUPPORTED_ARGS):
        for args in SUPPORTED_ARGS:
            if arg not in args_split:
                print(f"Missing [{arg}]")
        return True
def get_args(args):
    args_split = dict([tuple(arg.split("=")) if "=" in arg else (None, None) for arg in args])
    if check_args_or_fail(args_split):
        return
    # We have all args now continue 
def main():
    if len(sys.argv) == 1:
        print("Not enough args")
        return
    get_args(sys.argv[1:])

if __name__ == "__main__":
    main()
