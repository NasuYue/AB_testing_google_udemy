# Task 10
# 1. Find the Total Plays for the New England Patriots, and assign the result to "patriots_total_plays_count".
# 2. Find the Total Yards for the Seahawks, and assign the result to "seahawks_total_yards_count".

import requests
from bs4 import BeautifulSoup

response = requests.get("http://dataquestio.github.io/web-scraping-pages/2014_super_bowl.html")
content = response.content
parser = BeautifulSoup(content, 'html.parser')

patriots_total_plays_count=parser.select("#total-plays td")[2].text

seahawks_total_yards_count=parser.select("#total-yards td")[1].text


