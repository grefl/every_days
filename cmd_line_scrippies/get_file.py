#!/usr/bin/env python3
import urllib.error
import urllib.parse
import urllib.request
import sys


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

def fetch_and_write():
    url = None
    file_name = None
    args_len = len(sys.argv)
    if args_len == 1:
        print('please provide a url')
        return
    elif args_len == 2:
            url = sys.argv[1]
    elif args_len == 3:
            url, file_name = sys.argv[1]

    file_name = file_name if file_name else url.split('/').pop()
    req = RemoteGitFetch()
    res = req.fetch(url) 
    with open(f"./{file_name}", 'w+') as f:
      f.write(res)
      print(f'finished writing {file_name}')


fetch_and_write()
