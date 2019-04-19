from bs4 import BeautifulSoup
import requests

url = 'https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign=10'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
# print(soup.prettify())

horoscope_paragraph = soup.find_all('p')
print('Horoscope for Capricorn : Dec 22 - Jan 19')
print(horoscope_paragraph[0].text)
