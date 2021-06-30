special_ident = ['px', 'em', 'rem']
special_symbols = ['%', '!', ',', '~', '@']
class lexer():
  def __init__(self):
    self.input = None
    self.position = 0
    self.read_position = 0
    self.ch = None
    self.seen_colon = False
    self.in_brace = False
    self.special_symbols = special_symbols

  def reset(self, input):
    self.input = input
    self.ch = None
    self.seen_colon = False
    self.read_position = 0
    self.position = 0
    self.read_char()

  def parse_css(self, s):
    html = []
    l = lexer()

    for line in s.split('\n'):
      l.reset(line)
      temp_str = []

      while l.ch:
        temp_str.append(l.next_token()['literal'])
      html.append(''.join(temp_str))

    return '\n'.join(html)

  def read_char(self):
 
    if self.read_position >= len(self.input):
      self.ch = None
    else: 
      self.ch = self.input[self.read_position]

    self.position = self.read_position
    self.read_position +=1

  def eof(self):

    if self.read_position >= len(self.input):
      return True
    else:
      return False
       
  def peek(self):
  
    if self.eof():
      return 0
    else:
      return self.input[self.read_position]

  def is_white_space(self, ch):
    return ch == ' ' or ch == '\t' or ch == '\n' or ch == '\r'

  def is_letter(self, ch):
    return ch >= 'a' and ch <= 'z' or ch >= 'A' and ch <= 'Z' or ch == '_' or ch == '-'

  def is_number(self, ch):
    return ch.isnumeric()

  def read_number(self):
    start = self.position
    self.read_char()

    while self.is_number(self.ch):
      self.read_char()

    return self.input[start:self.position]
  def read_generic(self, ident):

    start = self.position
    self.read_char()

    while self.ch and self.ch != ident:
      print(self.ch)
      self.read_char()

    return self.input[start:self.read_position]
  def read_literal(self):

    start = self.position
    self.read_char()

    while self.is_letter(self.ch):
      self.read_char()

    return self.input[start:self.position]

  def next_token(self):
    tok = None
    if self.ch == '.' or self.ch == '#':
      if self.is_letter(self.peek()):
        literal = self.read_literal() 
        if literal:
          tok = {'type': 'NAME', 'literal': span(literal, 'name')}
          return tok
        else:
          tok = {'type': 'whoops', 'literal': span(literal, 'whoops') }
      else:
        tok = {'type': 'unknown', 'literal': span(self.ch, 'dot') }
    # TODO(greg) probably could just put this in a dict
    elif self.ch == '{':
      self.in_brace = True
      tok = token(self.ch, 'LBRACE', 'brace')
    elif self.ch == '}':
      self.in_brace = False
      tok = token(self.ch, 'RBRACE', 'brace')
    elif self.ch == '(':
      tok = token(self.ch, 'LPAREN', 'paren')
    elif self.ch == ')':
      tok = token(self.ch, 'RPAREN', 'paren')
    elif self.ch == '[':
      tok = token(self.ch, 'LBRACKET', 'bracket')
    elif self.ch == ']':
      tok = token(self.ch, 'RBRACKET', 'bracket')
    elif self.ch == ':':
      self.seen_colon = not self.seen_colon
      tok = token(self.ch, 'COLON', 'colon')
    elif self.ch == ';':
      tok = token(self.ch, 'SEMICOLON', 'colon')
    elif self.is_white_space(self.ch): 
      tok = {'type': 'WHITESPACE', 'literal': self.ch }
    elif self.is_letter(self.ch):

      literal = self.read_literal()
      if not self.in_brace:
        return token(literal, 'TAG', 'tag')

      global special_ident
      if literal in special_ident:
        return token(literal, 'KEYWORD', 'keyword') 
      else:
        if self.seen_colon:
          return token(literal, 'VALUE', 'value')
        else:
          return token(literal, 'PROP', 'prop')

    elif self.is_number(self.ch):
      number = self.read_number();
      return token(number, 'NUMBER', 'number')
    elif self.ch == '"':
      literal = self.read_generic('"')
      tok = token(literal, 'STRING', 'string')
    elif self.ch == "'":
      literal = self.read_generic("'")
      print(literal)
      tok = token(literal, 'STRING', 'string')
    else: 
      if self.ch in self.special_symbols:
        tok = token(self.ch,'SYMBOL', 'symbol')
      else:
        tok = {'type': 'unknown', 'literal': span(self.ch, 'unknown') }

    self.read_char()

    return tok

def span(text, class_name): 
  return f"<span class='{class_name}'>{text}</span>"

def token(literal, token_type, class_name):
  return {'type': token_type, 'literal': span(literal, class_name)}
