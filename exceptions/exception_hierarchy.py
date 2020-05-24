# Exception hierarchy using Web Scraping : Requests and Beautiful Soup

import requests
from bs4 import BeautifulSoup

url = "https://docs.python.org/2/library/exceptions.html"
response = requests.get(url)
# print(response.text)

# # 200 status code is for success.
# print(response.status_code)
# # Checks if any restrictions or not.
# print(response.ok)

soup = BeautifulSoup(response.content, "html.parser")
# print(soup.prettify())

print("Exception Hierarchy in Python : ")

pre_items = soup.find_all("pre")
for pre_item in pre_items:
    print(pre_item.text)
