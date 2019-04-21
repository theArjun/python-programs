# Web Scraping of Online Khabar

# First import requests, bs4

import requests
import bs4
from bs4 import BeautifulSoup

res = requests.get('https://www.onlinekhabar.com/')
type(res)
# It is a requests object.

help(res)

# Prints the whole text retrieved from response
print(res.text)

# Remember to pass res.text or res.content, not res only. It accepts text
# format not requests object.

soup = BeautifulSoup(res.text, 'lxml')

# Formatting the HTML content
print(soup.prettify())

#  Links in Online Khabar
for links in soup.find_all('a', string=True):
    print(links.getText())

# Paragraphs in Online Khabar
for paragraphs in soup.find_all('p'):
    print(paragraphs.getText())
    print('\n'*2)
