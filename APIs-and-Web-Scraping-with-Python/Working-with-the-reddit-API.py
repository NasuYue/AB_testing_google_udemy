# Task
# 1. Retrieving a list of trending posts on a particular subreddit
# 2. Exploring the comments on a single article
# 3. Posting your own comment on an article

import requests

# Create a dictionary of headers containing our Authorization header. 'bearer' refer to we're using OAuth
headers={"Authorization": "bearer 13426216-4U1ckno9J5AiK72VRbpEeBaMSKk", "User-Agent": "Dataquest/1.0"}
params={"t":"day"}
url="https://oauth.reddit.com/r/python/top"

# Make a GET request to the GitHub API with our headers.
# This API endpoint will give us details about Vik Paruchuri.
response=requests.get(url,headers=headers,params=params)

# Print the content of the response.  As you can see, this token corresponds to the account of Vik Paruchuri.
python_top=response.json()


# Major request type: get, post(201), patch(200), delete(204)
# Json: loads(), dumps()
