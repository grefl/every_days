from pathlib import Path
import sys
from fetch import Request


class RemoteGitFetch:
    def __init__(self):
        self.req = Request()
        self.raw_url = "https://raw.githubusercontent.com"
    
    def fetch(self, url):
        headers = {'Accept': 'application/json' }
        normalized_url = self.normalize_url(url)
        return self.req.get(normalized_url, {'data': None, 'headers': headers}) 

    def normalize_url(self, url):
        if 'github' in url:
            end = ''.join(url.split('.com')[1].split('/blob'))
            new_url = self.raw_url + end
            return new_url

        else: 
            return url.replace('blob', 'raw')

class CalcLines:
    def __init__(self,file_name):
        self.remote_fetch = RemoteGitFetch()
        self.type = 'remote' if 'https' in file_name else 'fs' 
        self.file_name = file_name

    def get_file_string(self, name):
            try:
               return Path(name).read_text()
            except FileNotFoundError:
                return f"ERROR: '{file_name}' not found"

    def get_file_from_web(self, url):
        return self.remote_fetch.fetch(url) 

    def normalize_url(self, url):
        if self.type == 'github':
            end = ''.join(url.split('.com')[1].split('/blob'))
            new_url = raw_url + end
            return new_url

        else: 
            return url.replace('blob', 'raw')
        
    def calc_lines(self, string):
        try:
            lines_without_empty_space = [line for line in string.split('\n') if line]
            line_count = len(lines_without_empty_space) 

            return line_count

        except FileNotFoundError:
            raise Error(f"ERROR: '{file_name}' not found")


    def sloccount(self):
        if self.type not in ['remote', 'fs']:
            raise Error(f"{self.type} is not a valid type")

        string = None
        if self.type == 'remote':
            string = self.get_file_from_web(self.file_name)
        else:
            string = self.get_file_string(self.file_name)

        if not string:
            raise Error("string is None")
        line_count = self.calc_lines(string)
        return line_count

url = 'https://github.com/grefl/every_days/blob/master/my_python_libs/get_file.py'        
calc = CalcLines(file_name = url)
print(calc.sloccount())
