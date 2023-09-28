#%%
from bs4 import BeautifulSoup as bs
import requests as rq
headers = {"User-Agent":"Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/117.0"}
s = rq.get("https://www.whitehouse.gov",headers=headers)
g = bs(s.text)
s.url
# %%
print(g.prettify())
# %%
ad = g.find_all('img')
print(ad)
# %%
print(len(ad))
# %%
print(dir(ad[0]))
# %%
dir(ad[0])
# %%
ad[0].attrs

# %%
for x in ad:
    print(x.attrs.__repr__())
    #print(x.attrs['href'] if x.attrs['href'] else 'none')
# %%
print(g.prettify())
# %%
print(g.find_all('div'))
# %%
r = requests.get('https://www.dotdashmeridith.com' + ad[5].attrs['src'])
if r.status_code == 200:
    with open('/home/nwsk/projects/theimage.jpg', 'wb') as f:
        for chunk in r.iter_content(1024):
            print('writing f')
            f.write(chunk)

# %%
dir(r)
# %%
r.url

# %%
from PIL import Image
i = Image.open('/home/nwsk/projects/theimage.jpg')
i.show()
# %%
r.status_code
# %%
s.url
# %%
from requests_html import AsyncHTMLSession

session = AsyncHTMLSession()

#r = session.get('https://www.google.com/?q=photon')
url = 'https://www.google.com/?q=photon'
r = await session.get(url).result().arender()
#As a bonus this wraps BeautifulSoup, I think, so you can do things like

#r.html.find('#myElementID').text

# %%
dir(r)
# %%
import pyppeteer
# %%
browser = await pyppeteer.launch(ignoreHTTPSErrors=not(True), headless=True)

# %%
