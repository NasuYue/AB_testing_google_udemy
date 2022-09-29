import csv

header=[]
games=[]

with open('game_sales.csv') as f:
    reader=csv.reader(f)
    rows=list(reader)
    header=rows[0]
    games=rows[1:]

gs={}
for x in games:
    gs[x[0]]=float(x[-1])
    
most_sold_game=sorted(gs.items(), key=lambda x:x[1],reverse=True)[0]
most_sold_game=most_sold_game[0]
