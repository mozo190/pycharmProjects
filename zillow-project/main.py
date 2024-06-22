import os

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

price = soup.find_all("span", {"data-test": "property-card-price"})
prices = [p.getText(strip=True).rstrip('+').rstrip('/mo').strip() for p in price]
print(prices)
for p in prices:
    print(p)

# props_link = soup.find_all("a", class_="property-card-link")
# paths = [link['href'] for link in props_link]
# for link in paths:
#     print(link)
