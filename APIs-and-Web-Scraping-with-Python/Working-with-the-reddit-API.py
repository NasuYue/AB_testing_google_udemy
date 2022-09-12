# ===== Task 1 ===== 
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

# Note: 
# Major request type: get, post(201), patch(200), delete(204)
# Json: loads(), dumps()

# ===== Task 2: find id with the most upvotes =====
# Article item: data > children > {kind,data}
python_top_articles=python_top['data']['children']

print(type(python_top_articles[0]))
print(len(python_top_articles))

most_upvoted = ""
most_upvotes = 0
for item in python_top_articles:
    if item['data']['ups']>most_upvotes:
        most_upvoted=item['data']['id']
        most_upvotes=item['data']['ups']
    
print(most_upvoted)
print(most_upvotes)


# ===== Task 4: Getting Post Comments =====
# Follow reddit API "https://oauth.reddit.com/" and "/r/{subreddit}/comments/{article}" endpoint
# Reference: https://old.reddit.com/dev/api#GET_comments_{article}

new_adr='https://oauth.reddit.com/r/python/comments/4b7w9u'
comments=requests.get(new_adr,headers=headers).json()

# ==== Task 5: Getting the Most Upvoted Comment ====

# Explore comments structure and find list of comment in 2nd item
comments_list=comments[1]['data']['children']

# Use Task 2 methold to find the most upvoted comment
most_ups=0
most_upvoted_comment=0
for x in comments_list:
    if x['data']['ups'] > most_ups:
        most_ups=x['data']['ups']
        most_upvoted_comment=x['data']['id']

# ==== Task 6: Upvoting a Comment ====
# Use id='d16y4ry' from task 5

url='https://oauth.reddit.com/api/vote'
payload={'id':'d16y4ry', 'dir':1}

response=requests.post(url,json=payload,headers=headers)

status=response.status_code