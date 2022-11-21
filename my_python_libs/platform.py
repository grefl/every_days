import pprint
import unittest

os_patterns = { 
        'Android': { 'offset': 0, 'end_char': {';': ';'}}, 
        'Windows': { 'offset': 3, 'end_char': {';': ';'}},
        'Linux': { 'offset': 0, 'end_char': {')': ')', ';': ';'}}, 
        }

def index_of(string, element_to_find, starting_index = 0):

    idx = starting_index 
    offset = len(element_to_find)
    while idx + offset - 1 < len(string):
        if string[idx : idx + offset] == element_to_find:
            return idx
        idx +=1
    return None

def parse_until(string: str, chars = {' ': ' '} ):
    i = 0
    length =  len(string)
    substring = []
    while i < length and string[i] not in chars: 
        substring.append(string[i])
        i +=1
    return ''.join(substring)

def get_layout_engine(user_agent: str):
    guesses = [
      { 'name': 'EdgeHTML', 'pattern': 'Edge' },
      {'name': 'Trident', 'pattern': 'Trident'},
      { 'name': 'Webkit', 'pattern': 'AppleWebKit' },
      {'name':'iCab', 'pattern': 'iCab'},
      #'Presto',
      # 'NetFront',
      # 'Tasman',
      # 'KHTML',
      {'name': 'Gecko', 'pattern': 'Gecko'},
    ]  
    for guess in guesses:
        if guess['pattern'] in user_agent:
            return guess['name'] 
    return None

def get_os_name(user_agent: str):
    guesses = [
      {'name': 'Android', 'pattern': 'Android'},
      {'name': 'Linux', 'pattern': 'Linux'},
      {'name': 'Windows', 'pattern': 'Windows'},
    ]  
    for guess in guesses:
        if guess['pattern'] in user_agent:
            offset = os_patterns[guess['name']]['offset']
            end_char = os_patterns[guess['name']]['end_char']
            index = index_of(user_agent, guess['pattern']) + len(guess['pattern']) + 1 + offset # + 1 for the space 
            version = parse_until(user_agent[index:], end_char)
            return { 'name': guess['name'], 'version': version }
    return None

def get_browser_name(user_agent):
    guesses = [
            {'name': 'Edge','pattern': 'Edg'},
            {'name': 'SamsungBrowser','pattern': 'SamsungBrowser'},
            {'name': 'Chrome','pattern': 'Chrome'},
            {'name': 'Firefox','pattern': 'Firefox'},
            ]
    for guess in guesses:
        if guess['pattern'] in user_agent:
            index = index_of(user_agent, guess['pattern']) + len(guess['pattern']) + 1 # + 1 for the '/' 
            version = parse_until(user_agent[index:])
            return {'name': guess['name'], 'version': version}
    return None

def parse_user_agent(user_agent: str):
    data = {
            'os': None,
            'layout_engine': None,
            'browser': None,
            }
    data['os'] = get_os_name(user_agent) 
    data['layout_engine'] = get_layout_engine(user_agent)
    data['browser'] = get_browser_name(user_agent)
    return data 

class Test(unittest.TestCase):
    def setUp(self):
       self.USER_AGENT_CHROME  = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36' 
       self.USER_AGENT_FIREFOX = 'Mozilla/5.0 (X11; Linux x86_64; rv:105.0) Gecko/20100101 Firefox/105.0'
       self.USER_AGENT_EDGE    = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36 Edg/83.0.478.37'
       self.USER_AGENT_SAMSUNG = 'Mozilla/5.0 (Linux; Android 5.0.2; SAMSUNG SM-G925F Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/4.0 Chrome/44.0.2403.133 Mobile Safari/537.36'

    def test_browser(self):
        chrome  = parse_user_agent(self.USER_AGENT_CHROME)
        self.assertEqual(chrome['browser']['name'], 'Chrome')

        firefox = parse_user_agent(self.USER_AGENT_FIREFOX)
        self.assertEqual(firefox['browser']['name'], 'Firefox')
        self.assertEqual(firefox['browser']['version'], '105.0')

        edge = parse_user_agent(self.USER_AGENT_EDGE)
        self.assertEqual(edge['browser']['name'], 'Edge')
        self.assertEqual(edge['browser']['version'], '83.0.478.37')

        samsung = parse_user_agent(self.USER_AGENT_SAMSUNG)
        self.assertEqual(samsung['browser']['name'], 'SamsungBrowser')
        self.assertEqual(samsung['browser']['version'], '4.0')
        self.assertEqual(samsung['os']['name'], 'Android')

    def test_os(self):
        chrome = parse_user_agent(self.USER_AGENT_CHROME)
        self.assertEqual(chrome['os']['name'], 'Linux')

        edge = parse_user_agent(self.USER_AGENT_EDGE)
        self.assertEqual(edge['os']['name'], 'Windows')
        self.assertEqual(edge['os']['version'], '10.0')

        android = parse_user_agent(self.USER_AGENT_SAMSUNG)
        self.assertEqual(android['os']['name'], 'Android')
        self.assertEqual(android['os']['version'], '5.0.2')

    def test_layout_engine(self):
        chrome = parse_user_agent(self.USER_AGENT_CHROME)
        self.assertEqual(chrome['layout_engine'], 'Webkit')
        edge = parse_user_agent(self.USER_AGENT_FIREFOX)
        self.assertEqual(edge['layout_engine'], 'Gecko')

def main():

    res = parse_user_agent(USER_AGENT_EDGE)
    pprint.pprint(res, indent = 4)


if __name__ == "__main__":
    # main()
    unittest.main()

