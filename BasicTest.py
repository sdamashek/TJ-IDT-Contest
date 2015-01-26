'''
BasicTest.py
Some simple tests on the website's status and search for 
wanted keywords with Requests
'''

import requests

class BasicTest():
    #Initialize a testcase with the given url
    def __init__(self, url):
        if isinstance(url, str):
            if url[0:4] != 'http':
                url = 'http://{0}'.format(url)
            self.url = url.lower()
        else: raise NotImplementedError
        
        self.page = requests.get(url)

    def teststatus(self):
        if 3 < self.page.status_code//100 < 6:
            return False
        else: return True
    
    def testkeyword(self, keyword):
        if keyword in self.page.text:
            return True
        else: return False


if __name__ == '__main__':
    t = BasicTest('http://localhost:8080/version1/menu.html')
    print(t.teststatus())
    print(t.testkeyword('Not Found'))

