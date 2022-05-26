import sys
from pprint import pprint
from fun import lex
for line in sys.stdin:
    if line.strip() == 'q':
        break
    else:
        pprint(lex('stdin', line.strip()))

