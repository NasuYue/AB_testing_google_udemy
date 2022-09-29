import csv
import os

header=[]
games=[]

data_dir = os.path.dirname(__file__)
file_path = os.path.join(data_dir, 'game_sales.csv')

with open(file_path, mode='r', encoding="utf-8") as f:
    reader=csv.reader(f)
    rows=list(reader)
    header=rows[0]
    games=rows[1:]

gs={}
for x in games:
    gs[x[0]]=float(x[-1])
    
most_sold_game=sorted(gs.items(), key=lambda x:x[1],reverse=True)[0]
# Tips: one line sorting a dict by desc

most_sold_game=most_sold_game[0]

print(most_sold_game)
