# Article location: data>children> {kind,data}
python_top_articles=python_top['data']['children']

print(type(python_top_articles[0]))
print(len(python_top_articles))
#print(python_top_articles[0]['ups'])

print([ x['data']['ups'] for x in python_top_articles])


top_upvotes=0
most_upvoted=0
for item in python_top_articles:
    if item['data']['ups']>top_upvotes:
        top_upvotes=item['data']['ups']
        most_upvoted=item['data']['id']
    
print(top_upvotes)
print(most_upvoted)