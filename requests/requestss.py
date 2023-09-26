#%%
# import requests module
import requests
from bs4 import BeautifulSoup as bs
#Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/117.0
headers = {"User-Agent":"Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/117.0"}
# create a session object
s = requests.Session()
 
# make a get request
#r = s.get('https://www.pexels.com/search/free%20wallpaper/',headers=headers)

#%%
#r = s.get('https://pixabay.com/images/search/wallpaper/',headers=headers)
#r = s.get('https://www.freepik.com/free-photos-vectors/wallpaper',headers=headers)
# <a class="tag-item" href="https://www.freepik.com/free-photos-vectors/flower-wallpaper
#https://www.freepik.com/free-photos-vectors/flower-wallpaper
r = s.get('https://www.freepik.com/free-photos-vectors/flower-wallpaper',headers=headers)

soup = bs(r.text)
# %%
print(soup.prettify())


# %%
ad = soup.find_all('a')

# %%
ad

# %%
r = s.get('https://www.freepik.com/ai/images',headers=headers)

#https://www.freepik.com/ai/images
# %%
soup = bs(r.text)

# %%
ad[30]
# %%
ad[50]
# %%
ad[50]['href']
# %%
print(ad[50].prettify())
# %%
