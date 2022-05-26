#!/bin/env python3
import unittest

def check_args_or_fail(args_split, supported_args):
    if any(True if arg not in args_split else False for arg in supported_args):
        for arg in supported_args: 
            if arg not in args_split:
                print(f"Missing [{arg}]")
        return True
    
def get_args(args, supported_args):
    args_split = dict([tuple(arg.split("=")) if "=" in arg else (None, None) for arg in args])
    if check_args_or_fail(args_split, supported_args):
        raise Exception("Missing args") 
    # We have all args so return them in a dictionary 
    return args_split

def tinyargs(args, supported_args):

    return get_args(args, supported_args)



        
def main():
    if len(sys.argv) == 1:
        print("Not enough args")
        return
    formatted_args = get_args(sys.argv[1:])
    tickets_search(formatted_args)


class TestArgs(unittest.TestCase):
    def testArgs(self):
        test_args = '--time-from=2008-07-20T22:55:29Z --time-to=2008-07-20T22:55:29Z'.split(' ')
        supported_args = ['--time-from', '--time-to']
        expected = dict([('--time-from', '2008-07-20T22:55:29Z'), ('--time-to', '2008-07-20T22:55:29Z')])
        self.assertEqual(expected, tinyargs(test_args, supported_args))

if __name__ == "__main__":
    unittest.main()


