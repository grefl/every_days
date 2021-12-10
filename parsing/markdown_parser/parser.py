from pathlib import Path
import sys
def create_header(index,text):
    return f'<h{index}>{text}</h{index}>' 

def get_file_name(): 
    if len(sys.argv) <= 1:
        print('Please provide a filename')
        return None
    file_name = sys.argv[1]
    if not file_name.endswith('.md'):
        print('Please provide a .md file')
        return None
    return file_name

def main():
    file_name = get_file_name()
    if not file_name:
        return
    string = Path(f'./{file_name}').read_text()
    p = Parser(str(string))
    p.parse()

class Parser():
    def __init__(self, text):
        self.text = text.split('\n') 
        self.line = 0
        self.line_idx = 0
        self.len = len(self.text)
        self.char = None
        self.html = []
        self.is_start_of_line = True 
    def get_line(self, start):
        while self.char != '\n':
            self.index += 1
            self.char = self.text[self.index]
        return self.text[start:self.index] 
    def parse(self):
        print(self.text)
        while self.line < self.len:
            print(f'line: {self.line} {self.len}')
            text = self.text[self.line]
            print(text)
            i = 0 
            print(f'i {i} text length: {len(text)}')

            if len(text) == 0:
                self.line +=1
                continue
            self.char = text[i]
            self.is_start_of_line = True
            if self.char == '#' and self.is_start_of_line:
                self.is_start_of_line = False
                num_hashes = 0 
                while self.char == '#':
                    i +=1
                    num_hashes +=1
                    self.char = text[i] 
                self.html.append(create_header(num_hashes, text[i:]))
                self.line +=1
                continue
            elif self.char.isalpha():
                print('yoyo')
                self.html.append(f'<p>{text[i:]}</p>')
                self.line +=1
            elif self.char == '>':

                self.html.append(f'<blockquote>{text[i+1:]}</blockquote>')
                self.line +=1
            else:
                print('else')
                print(text)
                break
            self.line +=1
        print('here')
        print(self.html)
        print('\n'.join(self.html))
        finished = Path('./res.html')
        finished.write_text('\n'.join(self.html)) 
if __name__ == '__main__':

    main()


