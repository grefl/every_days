import urllib.error
import urllib.parse
import urllib.request





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
