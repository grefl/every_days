#!/usr/bin/env python3
import urllib.error
import urllib.parse
import urllib.request
from pprint import pformat, pprint
import json
import sys

# only using this if in DIR_MODE
def get_api_url(owner, repo, path):
    return f"https://api.github.com/repos/{owner}/{repo}/contents/{path}"

raw_url = "https://raw.githubusercontent.com"
DIR_MODE= None
class Request():
  def __init__(self):
    self.method = 'GET'
    self.headers = {}
    self.data = {}
    self.params = {}
    
 

  def get(self, url, options): 
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
def parse_args(args):
    """
    returns -> url, file_name, mode
    { type: 'FILE' | 'DIR', file_name: str | None, owner: str | None, repo: str | None }
    """
    args_len = len(args)
    if args_len == 1:
        print('please provide a url')
        return
    elif args_len == 2:
            url = args[1]
            file_name = url.split('/').pop()
            return { 'type': 'FILE',
                      'file_name': file_name,
                      'owner': None,
                      'repo': None,
                   } 
    elif args_len == 3:
            global DIR_MODE
            # parse the filename or DIR_MODE
            url, file_name, mode = args[1:]
            if 'tree' in url.split('/'):
                rest = url.split('github.com/').pop()
                owner, repo = rest.split('/')
                return { 'type': 'DIR',
                        'file_name': rest.split('master/').pop(),
                        'owner': owner,
                        'repo': repo,
                        }
            else:
                file_name = url.split('/').pop()
                return { 'type': 'DIR',
                         'file_name': file_name,
                         'owner': None,
                         'repo': None,
                        } 
def fetch_api(url):
    print(url)
    return
    req = Request()
    headers = { 'Accept': 'application/vnd.github.v3+json' }
    options = {'data': None, 'headers': headers}
    res = req.get(url,options) 
    return res

def fetch_website(url):
    req = Request()
    headers = {'Accept': 'application/json' }
    options = {'data': None, 'headers': headers}
    end = ''.join(url.split('.com')[1].split('/blob'))
    res = req.get(url + end, options)
    return res
def fetch_and_write():
    url = None
    file_name = None
    global DIR_MODE 
    data =  parse_args(sys.argv)
    print(data)
    res = None
    if data['type'] == 'DIR':
        res = fetch_api(get_api_url(data['owner'], data['repo'], data['file_name']))
    else:
        res = fetch_website(data[''], data['file_name'])
    if res:
        with open(f"./test_output", 'w+') as f:
            f.write(res)
            print(f'finished writing')


fetch_and_write()
