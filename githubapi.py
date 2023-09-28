#%%
from github import Github

# Authentication is defined via github.Auth
from github import Auth

# using an access token
auth = Auth.Token("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")

# First create a Github instance:

# Public Web Github
g = Github(auth=auth)

# Github Enterprise with custom hostname
g = Github(base_url="https://github.com/api/v3", auth=auth)


# Then play with your Github objects:
for repo in g.get_user().get_repos():
    print(repo.name)

# To close connections after use
g.close()

# %%
#```python
from gitsuggest import GitSuggest

# To use with username password combination
#gs = GitSuggest(username=<username>, password=<password>)


gs = GitSuggest(token="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")

# To use without authenticating
#gs = GitSuggest(username=<username>)

# To use with deep dive flag
#gs = GitSuggest(username=<username>, password=<password>, token=None, deep_dive=True)
gs = GitSuggest(token="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")
#gs = GitSuggest(username=<username>, deep_dive=True)

# To get an iterator over suggested repositories.
m = gs.get_suggested_repositories()
#n = gs.Github.github.get_repos()
#%%
import os
os.listdir
# %%
os.curdir = '/home/nwsk/projects/gitsuggest'
# %%
os.curdir
# %%
m
# %%
for x in m:
    print(x)
# %%
len(m)
# %%
m.__next__()

# %%
import requests
import json
r = requests.get('https://api.github.com/repos/django/django')
if(r.ok):
    repoItem = json.loads(r.text or r.content)
    print("Django repository created: " + repoItem['created_at'])
# %%
from github import Github

# Authentication is defined via github.Auth
from github import Auth

# using an access token
auth = Auth.Token("xxx")

# First create a Github instance:

# Public Web Github
import time
g = Github(auth=auth)
repositories = g.search_repositories(query='language:python')
repos = []
for repo in repositories:
    repos.append(repo)
    print(repo)
    if len(repos) % 300 == 0:
        print('300 reached waiting 60*2 seconds')
        time.sleep(120)
#%%
rp = g.get_repo(repos[0])
# %%
# %%
repos
# %%
len(repos)
# %%
