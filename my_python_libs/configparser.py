from pathlib import Path

class ConfigParser():
    def __init__(self, delimiter =' = '):
        self.sections = {}
        self.delimiter = delimiter

    def add_section(self, section):
        self.sections[section] = {}
    def add(self, section, key, value):
        self.sections[section][key] = value
    def write(self, file_name):
        pre_string = [] 
        for section in config.sections:
            pre_string.append(f'[{section}]\n')

            for key, value in config.sections[section].items():
                value = config.delimiter + value
                pre_string.append(f'{key}{value}\n')
            pre_string.append('\n')
        string = "".join(pre_string)
        Path(file_name).write_text(string) 
    
config = ConfigParser()
config.add_section('owner')
config.add_section('database')
config.add('owner', 'name', 'John Doe')
config.add('owner', 'organization', 'Acme Widgets')
config.add('database', 'server', '192.168.0.49')
config.add('database', 'port', '143')
config.add('database', 'file', 'secrets.txt')
config.write('config')
