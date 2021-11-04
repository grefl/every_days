from pathlib import Path
import pprint

def search_for_files_recursively(path_start):
    return [path.resolve() for path in Path(path_start).rglob('*')] 
files = search_for_files_recursively('.')
for file in files:
    print(file)

