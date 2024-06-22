import os
import re

import requests
from bs4 import BeautifulSoup

sheet_research_link = os.environ.get('RESEARCH_LINK')
zillow_link = os.environ.get('ZILLOW_ClONE')

response = requests.get(zillow_link)
yc_web_page = response.text
# print(yc_web_page)

soup = BeautifulSoup(yc_web_page, "html.parser")

# print(soup.prettify())
address = soup.find_all("address", {"data-test": "property-card-addr"})

#strip=True removes the white spaces
# addresses = [a.getText(strip=True) for a in address]
# for a in addresses:
#     print(a)

price_elements = soup.find_all("span", {"data-test": "property-card-price"})


def trim_prices(price):
    match = re.search(r'(\d+(?:,\d{3})*)', price)
    if match:
        return price[:match.end()].strip()
    return price


prices = [trim_prices(p.getText(strip=True)) for p in price_elements]
for p in prices:
    print(p)

# props_link = soup.find_all("a", class_="property-card-link")
# paths = [link['href'] for link in props_link]
# for link in paths:
#     print(link)
