from pathlib import Path
import sys

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
def peek_text(text,i):
    if i == len(text) -1:
        return None 
    return text[i + 1]
def parse_line(text):
    start = 0
    i = 0
    IN = True
    OUT = False 
    double = False
    state = OUT
    temp = []
    bracket = [-1, -1]
    parens  = [-1, -1]
    while i < len(text):
        char = text[i]
        if char == '*' and state == OUT:
            state = IN
            start = i
            if i +1 < len(text) and text[i+1] == '*':
                double = True

        elif char == "*" and state == IN:
            if double:
                if i +1 < len(text) and text[i+1] == '*':
                    temp[start] = '<strong'
                    temp[start+1] = '>'
                    state = OUT
                    temp.append('</strong>')
                    i +=2
                    continue
                else:
                   temp.append(char)
                   i +=1
                   continue
            temp[start] = '<i>'
            state = OUT
            temp.append('</i>')
            i +=1
            continue
        elif char == '[':
            second_brackets = -1
            failed = False
            copy_i = i
            mini_i = 0
            temp_chars = []
            temp_chars.append(None)
            while copy_i < len(text):
                copy_char = text[copy_i]
                if copy_char == ']':
                    peeked = peek_text(text, copy_i)
                    if not peeked or peeked != '(':
                        failed = True
                        break 
                    second_brackets = mini_i 
                elif copy_char == ')':
                    temp.append(f'''<a href="{''.join(temp_chars[second_brackets+3:])}">''')
                    i_i = 2
                    while i_i <= second_brackets:
                        temp.append(temp_chars[i_i])
                        i_i +=1
                    temp.append('</a>')
                    i = copy_i + 1
                    break
                temp_chars.append(text[copy_i])
                mini_i +=1
                copy_i +=1
            if copy_i == len(text) or failed:
                continue

        if i > len(text) -1:
            break
        temp.append(text[i])
        i +=1
    return ''.join(temp) 

def create_header(index,text):
    return f'<h{index}>{parse_line(text)}</h{index}>' 

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
            # bug waiting to happen
            self.char = self.text[self.index]
        return self.text[start:self.index] 
    def parse_list(self):
        items = []
        while self.char == '-':
            items.append(f'<li>{parse_line(self.text[self.line][1:])}</li>')
            self.line +=1
            text = self.text[self.line]
            if len(text) == 0:
               break 
            self.char = text[0]

        joined_items = '\n'.join(items)
        self.html.append(f"""<ul>\n{joined_items}\n</ul>""")
    def parse(self):
        while self.line < self.len:
            text = self.text[self.line]
            i = 0 

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
                self.html.append(f'<p>{parse_line(text[i:])}</p>')
                self.line +=1
            elif self.char == '>':

                self.html.append(f'<blockquote>{parse_line(text[i+1:])}</blockquote>')
                self.line +=1
            elif self.char == '-': 
                # man this is bad
                self.parse_list()
                continue
            else:
                self.html.append(parse_line(text))
            self.line +=1
        finished = Path('./res.html')
        finished.write_text('\n'.join(self.html)) 
if __name__ == '__main__':

    main()


