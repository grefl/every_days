import os

# helpers
def find_index_of_first_equals(string):
    return string.index('=')
def get_string_from_file(file_name):
    string = None
    with open(f'./{file_name}') as f:
        string = f.read()
    return string

def keys_and_values(array):
    array_of_keys_and_values = []
    for env_str in array:
        index = find_index_of_first_equals(env_str)
        key = env_str[:index]
        value = env_str[index+1:]
        array_of_keys_and_values.append((key,value))
    return array_of_keys_and_values



def main():
    env_str = get_string_from_file('.env')
    values = keys_and_values([env_str for env_str in env_str.split('\n') if env_str])
    for (key, value) in values:
        os.environ[key] = value
    print(os.environ)


if __name__ == '__main__':
    main()
