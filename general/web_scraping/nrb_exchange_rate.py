import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import json

# Creating a fake user agent to send request to NRB website.
ua = UserAgent()
header = {"user-agent": ua.chrome}

# Requests response from NRB Website
url = "https://www.nrb.org.np/fxmexchangerate.php"
response = requests.get(url, headers=header)

# Checking the status code and if everything is okay.
print(response.status_code, response.ok)

# Creating soup object to parse the HTML of Exchange rate webpage.
soup = BeautifulSoup(response.content, "html.parser")

# Stores the data of every tables in Exchange Rate Webpage
stat_tables = soup.find_all("table")

# Checking how many tables are there ?
print(len(stat_tables))
# Oh, it was 8.

# Table no. 6 was desired table for exchange rate.
exchange_rate = stat_tables[6]

print(type(exchange_rate))
# bs4.element.Tag

# List of scraped currencies.
currencies = [
    "U.S. Dollar",
    "European Euro",
    "UK Pound Sterling",
    "Swiss Franc",
    "Australian Dollar",
    "Canadian Dollar",
    "Singapore Dollar",
    "Japanese Yen",
    "Chinese Yuan",
]

# List that stores the data of every currencies.
currency_exchange_rate = []

for i in range(2, 11):

    rows = exchange_rate.find_all("tr")
    country_currency = rows[i]
    country_currency_data = country_currency.find_all("td")

    # Temporary dictionary to store the buying and selling rates of currency
    # of a particular country.
    data = {}

    # Slicing from three characters removed the flag.
    # Scraping names from the website was too hard as text weren't properly formatted.
    data["currency"] = currencies[i - 2]

    # Nepali Unit was at last of the string.
    try:
        data["nepali_unit"] = int(country_currency_data[1].text)
    except (ValueError, IndexError):
        data["nepali_unit"] = "Undefined"

    try:
        data["buying_rate"] = float(country_currency_data[2].text)
    except (ValueError, IndexError):
        data["buying_rate"] = "Undefined"

    try:
        data["selling_rate"] = float(country_currency_data[3].text)
    except (ValueError, IndexError):
        data["selling_rate"] = "Undefined"

    currency_exchange_rate.append(data)

# Converting to JSON string with indentation 4
currency_json_data = json.dumps(currency_exchange_rate, indent=4)

# Writing the JSON string file
with open("currency_exchange_rate.json", "w") as exchange_rate:
    exchange_rate.write(currency_json_data)
