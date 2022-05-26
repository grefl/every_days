#!/bin/env python3 
from pathlib import Path
from dataclasses import dataclass
from enum import Enum
from pprint import pprint

# class Keywords(Enum):
#     Function = 'function'
#     Return   = 'return'
#     Let      = 'let'
#     None_    = 'none'
#     True_    = 'true'
#     False_   = 'false'
#     If       = 'if'
#     While    = 'While'
#     For      = 'For'

#     # GODAMMIT PYTHON! Y U DO DIS?
#     def __contains__(cls, item): 
#         try:
#             cls(item)
#         except ValueError:
#             return False
#         else:
#             return True

def is_ascii_alphanumeric(c):

    ascii_decimal = ord(c) 

    return (ascii_decimal >= 48 <= 57) | (ascii_decimal >= 65 and ascii_decimal <= 91) or (ascii_decimal >= 97 and ascii_decimal <= 122)  

class TokenType(Enum):
    LeftParen  = 0 
    RightParen = 1 
    LeftBrace  = 2 
    RightBrace = 3 
    Asign      = 4 
    Rubbish    = 5 
    Name       = 5 

    # So I might get rid of these and just call them 'Name' 
    # and figure out which one is in the parser. But I'm not sure,
    # it makes sense that I should identify the type of keyword now, since this will happen eventually 
    # NOTE(greg) Note to self, I change my mind just use 'Name'
    Function   =   6
    Return     =   7 
    Let        =   8 
    None_      =   9 
    True_      =   10 
    False_     =   11 
    If         =   12 
    While      =   13 
    For        =   14 


def consume_while(file_str, index, predicate):
    things = []
    while index < len(file_str) and predicate(c := file_str[index]):
        print('things')
        print(c, index, things)
        things.append(c)
        index +=1
    return "".join(things), index

# def lex_thing(file_id, file_str, index):
#     pass


@dataclass
class Token:
    file_id: str
    token_type: TokenType
    contents: str

# https://stackoverflow.com/a/196392
# I know there's an inbuilt method but I prefer this for learning purposes, ya know?
def is_ascii(str):
    return all(ord(c) < 128 for c in str)

def lex(file_id, file_str):
    output = []
    index = 0

    while index < len(file_str):
        c = file_str[index] 
        if c == '(':
            token = Token(file_id, TokenType.LeftParen, c)
            output.append(token)
            index +=1 
        elif c == ')':
            token = Token(file_id, TokenType.RightBrace, c)
            output.append(token)
            index +=1 
        elif c == '{':
            token = Token(file_id, TokenType.LeftBrace, c)
            output.append(token)
            index +=1 
        elif c == '}':
            token = Token(file_id, TokenType.RightBrace, c)
            output.append(token)
            index +=1 
        elif c == '=':
            token = Token(file_id, TokenType.Asign, c)
            output.append(token)
            index +=1 
        elif is_ascii_alphanumeric(c):
            thing, index = consume_while(file_str, index, is_ascii_alphanumeric)
            token = None
            if thing in Keywords:
                token= Token(file_id, Name, thing)
            output.append(token)
            print('is ascii')
        else:
            index +=1
    return output


def main():
    file_string = Path('./test.fake').read_text()
    pprint(lex('./test.fake', file_string))
if __name__ == '__main__':
    main()