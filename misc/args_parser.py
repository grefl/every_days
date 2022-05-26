#!/bin/env python3
import sys
from datetime import datetime
from tinyargs import tinyargs

SUPPORTED_ARGS = ['--time-from', '--time-to']

def get_tickets(amount = 100):
    return [{"created_at": "2008-07-20T22:55:29Z"} for _ in range(amount)]


def dt_convert(date_time_string):
    return datetime.strptime(date_time_string, "%Y-%m-%dT%H:%M:%S%z").date()

def in_between(start, ticket_time, end, predicate):
    return predicate(start) <= predicate(ticket_time) and predicate(end) >= predicate(ticket_time)

        
def main():
    if len(sys.argv) == 1:
        print("Not enough args")
        return
    args = tinyargs(sys.argv[1:], SUPPORTED_ARGS)
    tickets_search(args)

def tickets_search(args, amount = 100):
    time_from = args['--time-from']
    time_to = args['--time-to']
    tickets = get_tickets(amount)

    for ticket in tickets:
        print(in_between(time_from, ticket['created_at'], time_to, dt_convert))
if __name__ == "__main__":
    main()
   # test_args = '--time-from=2008-07-20T22:55:29Z --time-to=2008-07-20T22:55:29Z'
   # def wrapper():
   #     tickets_search(get_args(test_args), 200000)
   # bench(wrapper, 20)
