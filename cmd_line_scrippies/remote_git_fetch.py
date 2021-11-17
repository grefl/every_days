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

