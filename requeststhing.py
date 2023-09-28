from thing import Thing
import requests
from bs4 import BeautifulSoup


class GoogleRequestThing(Thing):
    def __init__(self, name=None, description="blank", typeName='RequestThing', status='New', *args, **kwargs):
        super().__init__(description=description, typeName=typeName, name=name,status=status)

    def use(self,query=None):
        print('Used query, it spits out:')
        self.status = "Used"

        headers_Get = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'DNT': '1',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1'
        }
        s = requests.Session()
        q = '+'.join(self.description.split() if query==None else query.split())
        url = 'https://www.google.com/search?q=' + q + '&ie=utf-8&oe=utf-8'
        r = s.get(url, headers=headers_Get)

        soup = BeautifulSoup(r.text, "html.parser")
        self.soup = soup
        return soup.text

    def useForText(self,query):
        soup = self.use(query)
        return soup.text

    
    