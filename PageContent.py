'''
PageContent.py
Storing the information of a webpage
Given that the content is valid (no 
'''
import requests, functools

@functools.total_ordering
class Page:
    def __init__(self, url, content = None):
        if isinstance(url, str):
        	if url[0:4] != 'http':
        		url = 'http://{0}'.format(url)
            self.url = url.lower()
        else: raise NotImplementedError

        if content == None:
            self.content = requests.get(self.url).text
        elif isinstance(content, str):
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
