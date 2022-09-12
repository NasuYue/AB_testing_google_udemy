# Task 8
# 1. Select all of the elements that have the class "outer-text". Assign the text of the first paragraph that has the class "outer-text" to "first_outer_text".
# 2. Select all of the elements that have the ID "second". Assign the text of the first paragraph that has the ID "second" to the variable "second_text".

import requests
from bs4 import BeautifulSoup

response = requests.get("http://dataquestio.github.io/web-scraping-pages/ids_and_classes.html")
content = response.content
parser = BeautifulSoup(content, 'html.parser')

# find_all: get a list by elements or class
# Equivalence: first_outer_text=parser.select(".outer-text")[0].text
first_outer_text=parser.find_all('p', class_='outer-text')[0].text


# bs.select([CSS selector])  
# .class ; #id ; p for paragraph ; div for tag
second_text=parser.select("#second")[0].text
