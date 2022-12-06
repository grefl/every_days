#!/usr/bin/env python3
import sys



def main():
    INWORD = False
    nc = 0
    nl = 0
    nw = 0
    input = sys.stdin.read()
    for c in input:
        nc +=1
        if c == '\n':
            nl +=1
        if c == ' ' or c == '\n' or c == '\t':
            INWORD = False
        elif not INWORD:
            INWORD = True
            nw +=1
    print(f"chars = {nc}, words = {nw}, lines = {nl}")
main()
