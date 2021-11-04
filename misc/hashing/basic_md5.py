#!/bin/env python3
import sys
from pathlib import Path
import os
import hashlib
import json

def add_file_to_hash(hashes, file_hash, file):
        if file_hash in hashes:
            hashes[file_hash].append(file)
        else: 
            hashes[file_hash] = [file]
            

def main():
    files = []
    raw_input = sys.stdin.read()
    files = [file.strip() for file in raw_input.split('\n') if file]
    hashes = {}
    for file in files:
        file_string = Path(file).read_text()
        file_hash = hashlib.md5(file_string.encode('utf-8')).hexdigest()
        add_file_to_hash(hashes, file_hash, file)

    duplicates = {}
    for (key, value) in hashes.items():
        if len(value) > 1:
            print(key, value)
            duplicates[key] = value
    with open ('./duplicates.json', 'w', encoding='utf-8') as json_file:
        json.dump(duplicates, json_file, ensure_ascii=False, indent=4)
            
if __name__ == '__main__':
    main()
