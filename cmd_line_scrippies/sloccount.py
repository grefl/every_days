#!/usr/bin/env python3
import sys
from pathlib import Path

def main():
    file_name = sys.argv[1]
    try:
        lines_without_empty_space = [line for line in Path(file_name).read_text().split('\n') if line]
        line_count = len(lines_without_empty_space) 
        print(line_count)
    except FileNotFoundError:
        print(f"ERROR: '{file_name}' not found")



if __name__ == '__main__':
    main()
