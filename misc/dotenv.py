import os
from pathlib import Path
import unittest

def index_of(string, element_to_find, starting_index = 0):

    idx = starting_index 
    offset = len(element_to_find)
    while idx + offset - 1 < len(string):
        if string[idx : idx + offset] == element_to_find:
            return idx
        idx +=1
    return None
# ============================
#          Helpers
# ============================

def find_index_of_first_equals(string):
    return index_of(string, '=')

def get_string_from_file(file_name):
    return Path(f'./{file_name}').read_text()

def get_keys_and_values(array):

    array_of_keys_and_values = []
    for env_str in array:
        index = find_index_of_first_equals(env_str)
        key = env_str[:index]
        value = env_str[index+1:]
        array_of_keys_and_values.append((key,value))

    return array_of_keys_and_values

def check_for_existing_env(string):
    index         = index_of(string,'$')
    start         = index
    bash_key_name = ''
    key           = ''
    index +=1
    while index < len(string) and (string[index].isupper() or string[index] == '_'):
        key += string[index]
        index +=1
    slice_start = '' if start == 0 else string[:start]
    slice_end   = '' if start + len(key) >= len(string) else string[start + len(key)+1:]
    env_value = os.getenv(key)
    
    return slice_start + env_value + slice_end if env_value else '' 

def parse_value(value, index_start = 0):
    index = index_of(value, '$', index_start)
    if index is None:
        return value

    existing_env_var = check_for_existing_env(value) 

    return parse_value(existing_env_var, index + 1) if existing_env_var else value

# ============================
#       Start program 
# ============================

def main(file_name):
    env_str = get_string_from_file(file_name)
    keys_and_values = get_keys_and_values([env_str for env_str in env_str.split('\n') if env_str])
    for (key, value) in keys_and_values:
        os.environ[key] = parse_value(value) 

# ============================
#          Testing 
# ============================

class Test(unittest.TestCase):
 
    def test_1(self):
        main('.env')
        value = os.getenv('GORB_SAYS')
        self.assertEqual(value, "I am GORB!")
        

    def test_2(self):
        main('.env')
        value = os.getenv('ROOT_URL')
        self.assertEqual(value, "~google.com/app/src")
    def test_3(self):
        main('.env')
        value = os.getenv('WWW')
        self.assertEqual(value, "en.www.google.com")

        

if __name__ == '__main__':
    # main('.env')
    unittest.main()
