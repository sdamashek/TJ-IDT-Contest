'''
PageContent.py
Storing the basic information of a webpage 
'''
from functools import total_ordering
from requests import get
from selenium import webdriver

@total_ordering
class Page:
    def __init__(self, url, content):
        self.url = url.lower()

        if isinstance(content, str):
            self.content = content
        else: raise NotImplementedError

    def _is_valid_operand(self, other):
        return hasattr(other, 'url') and hasattr(other, 'content')

    def __lt__(self, other):
        if not self._is_valid_operand(other):
            raise NotImplementedError
        
        return (self.url, self.content) < (other.url, other.content)

    def __eq__(self, other):
        if not self._is_valid_operand(other):
            raise NotImplementedError

        return (self.url, self.content) < (other.url, other.content)

    def __hash__(self):
        return hash( (self.url, self.content) )
## END OF CLASS

class NormalPage(Page):
    # the content will be represented by the title of the webpage
    # define additional information on wheteher the page is static
    def __init__(self, url, hyperlinks=[], is_static=True):
        driver = webdriver.Firefox()
        driver.get(url)

        Page.__init__(self, url, driver.title)
        driver.close()

        if isinstance(hyperlinks, list):
            self.links = sorted(hyperlinks)
        else: raise NotImplementedError
        self.is_static = is_static

    def cmp_links(self, other):
        if hasattr(other, links):
            if len(self.links) != len(other.links): return False
            else: return self.links == other.links
        else: raise NotImplementedError
## END OF CLASS

class ErrorPage(Page):
    # The content will the error Code in str
    def __init__(self, url, error):
        Page.__init__(self, url, error)
## END OF CLASS

# call the appropiate page class
# TODO: normalize the url, add additional checks on dynamic contents
#       and hyperlinks :-)
def new_page(url):
    if url[0:4] != 'http':
        url = 'http://{0}'.format(url)
        url = url.lower()
    
    r = requests.get(url)
    if 400 <= r.status_code < 600:
        print("HTTP error "+str(r.status_code)+" in "+url);
        return ErrorPage(url, "HTTP error "+str(r.status_code))
    else:
        return NormalPage(url)
## END
