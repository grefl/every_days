from html.parser import HTMLParser
import sys
import urllib.error
import urllib.parse
import urllib.request

class Request():
  def __init__(self):
    self.method = 'GET'
    self.headers = {}
    self.data = {}
    self.params = {}
    
 

  def get(self, url, options = {}): 
    if not options:
        options['data'] = None
        options['headers'] = {'Accept': 'text/plain'}
    req = urllib.request.Request(
      url,
      data=options['data'],
      headers=options['headers'],
      method=self.method
    )
    try:
      
      with urllib.request.urlopen(req) as res:
        return res.read().decode(res.headers.get_content_charset('utf-8'))
    except urllib.error.HTTPError as e:
      print(e)


class MyParser(HTMLParser):
  def init(self):
    self.packages = []
    self.package = {'name': None, 'version': None, 'description': None } 
    self.in_a = False
    self.in_name = False 
    self.in_version = False 
    self.in_description = False
  def reset(self):
    HTMLParser.reset(self)

  def handle_starttag(self, tag, attr):
    if tag == 'a' and find_val(attr, 'package-snippet'):
      self.in_a = True
    elif tag == 'span' and find_val(attr, 'package-snippet__name'):
      self.in_name = True
    elif tag == 'span' and find_val(attr, 'package-snippet__version'):
      self.in_version = True
    elif tag == 'p' and find_val(attr, 'package-snippet__description'):
      self.in_description = True
  def handle_endtag(self, tag):

    if self.in_a and tag == 'a':
      self.in_a = False
      self.packages.append(self.package)
      self.package = {'name': None, 'version': None, 'description': None }

    if self.in_a and self.in_name and tag == 'span':
      self.in_name = False

    if self.in_a and self.in_version and tag == 'span':
      self.in_version = False

    if self.in_a and self.in_description and tag == 'p':
      self.in_description = False

  def handle_data(self, data):
    if self.in_a and self.in_name:
        self.package['name'] = data

    if self.in_a and self.in_version:
      self.package['version'] = data
 
    if self.in_a and self.in_description:
      self.package['description'] = data

def find_val(l, val):
  for v in l:
    if v[1] == val:
      return True
  return False


p = MyParser()
p.init()
p.reset()
def find_val(l, val):
  for v in l:
    if v[1] == val:
      return True
  return False
search = sys.argv[1]
url = f'https://pypi.org/search?q={search}&page=2'
headers = {'Accept': 'application/json' }
options = {'data': None, 'headers': headers}

req = Request()
s = req.get(url, options)
for line in s.split('\n'):
  p.feed(line)
  p.reset()
# with open('./res.html') as f:
  # for line in f.readlines():
    #p.feed(line)
    # p.reset()


strings = []
for package in p.packages:
  left = f"{package['name']} ({package['version']})"  
  right =  f"{package['description']}"
  strings.append([left,right])
longest = 0
for left,right in strings:
    if len(left) > longest:
      longest = len(left)
print(''.ljust(longest + 20, '-'))
print("\n\n")
for (left, right) in strings:
  print(left.ljust(longest + 5, ' ') + right)

print("\n\n")
print(''.ljust(longest + 20, '-'))


