from pathlib import Path
import sys
from fetch import Request

raw_url = "https://raw.githubusercontent.com"


class CalcLines:
    def __init__(self,file_name, type = 'fs'):
        self.req = Request()
        self.type = type
        self.file_name = file_name
    def get_file_string(self, name):
            try:
               return Path(name).read_text()
            except FileNotFoundError:
                return f"ERROR: '{file_name}' not found"

    def get_github_file_string(self, url):
        headers = {'Accept': 'application/json' }
        end = ''.join(url.split('.com')[1].split('/blob'))
        new_url = raw_url + end
        return self.req.get(new_url, {'data': None, 'headers': headers}) 

    def calc_lines(self, string):
        try:
            lines_without_empty_space = [line for line in string.split('\n') if line]
            line_count = len(lines_without_empty_space) 

            return line_count

        except FileNotFoundError:
            raise Error(f"ERROR: '{file_name}' not found")


    def sloccount(self):
        if self.type not in ['fs', 'github']:
            raise Error(f"{self.type} is not a valid type")

        string = None
        if self.type == 'github':
            string = self.get_github_file_string(self.file_name)
        else:
            string = self.get_file_string(self.file_name)

        if not string:
            raise Error("string is None")
        line_count = self.calc_lines(string)
        return line_count
url = 'https://github.com/grefl/algorithms_and_data_structures/blob/main/playground/heap.py'        
calc = CalcLines(type='github', file_name = url)
assert calc.sloccount() == 48
