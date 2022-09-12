from cgitb import text
import requests
from bs4 import BeautifulSoup

url='http://dataquestio.github.io/web-scraping-pages/simple.html'
response=requests.get(url)
content=response.content

# Task 3: Get the text inside the title tag, and assign the result to title_text.
parser=BeautifulSoup(content,'html.parser')
body=parser.body
p=parser.p

# Use tag type 
title_text=parser.title.text

# ==== Task 4: Use find_all ====
title_text=parser.find_all('title')[0].text

# ==== Task 5: Elements ID ====
# Pass in the ID attribute to only get the element with that specific ID.
first_paragraph = parser.find_all("p", id="first")[0]
print(first_paragraph.text)

# Reference page: http://dataquestio.github.io/web-scraping-pages/simple_ids.html
second_paragraph_text = parser.find_all('p', id='second')[0].text

# ==== Task 6: Element Classes ==== 
# Get the website that contains classes.
response = requests.get("http://dataquestio.github.io/web-scraping-pages/simple_classes.html")
content = response.content
parser = BeautifulSoup(content, 'html.parser')

# Get the text in the second inner paragraph, and assign the result to second_inner_paragraph_text.
second_inner_paragraph_text = parser.find_all('p', class_='inner-text')[1].text

# Get the text of the first outer paragraph, and assign the result to first_outer_paragraph_text.
first_outer_paragraph_text = parser.find_all('p', class_='outer-text')[0].text