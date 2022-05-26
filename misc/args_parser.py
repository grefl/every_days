#!/bin/env python3
import sys
from datetime import datetime
from basic_bench import bench
SUPPORTED_ARGS = ['--time-from', '--time-to']

def get_tickets(amount = 100):
    return [{"created_at": "2008-07-20T22:55:29Z"} for _ in range(amount)]

def check_args_or_fail(args_split):
    if any(True if arg not in args_split else False for arg in SUPPORTED_ARGS):
        for arg in SUPPORTED_ARGS:
            if arg not in args_split:
                print(f"Missing [{arg}]")
        return True

def dt_convert(date_time_string):
    return datetime.strptime(date_time_string, "%Y-%m-%dT%H:%M:%S%z").date()

def in_between(start, ticket_time, end, predicate):
    return predicate(start) <= predicate(ticket_time) and predicate(end) >= predicate(ticket_time)

def get_args(args):
    args_split = dict([tuple(arg.split("=")) if "=" in arg else (None, None) for arg in args.split(' ')])
    if check_args_or_fail(args_split):
        raise Exception("Missing args") 
    # We have all args so return them in a dictionary 
    return args_split
        
def main():
    if len(sys.argv) == 1:
        print("Not enough args")
        return
    formatted_args = get_args(sys.argv[1:])
    tickets_search(formatted_args)

def tickets_search(args, amount = 100):
    time_from = args['--time-from']
    time_to = args['--time-to']
    tickets = get_tickets(amount)

    for ticket in tickets:
        in_between(time_from, ticket['created_at'], time_to, dt_convert)
if __name__ == "__main__":
    test_args = '--time-from=2008-07-20T22:55:29Z --time-to=2008-07-20T22:55:29Z'
    def wrapper():
        tickets_search(get_args(test_args))
    bench(wrapper, 200)
