from main import Request
from parser import MyParser
import sys


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

