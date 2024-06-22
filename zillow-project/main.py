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
address = soup.find_all("div", class_="address")
price = soup.find_all("div", class_="property-card-price")
props_link = soup.find_all("a", class_="property-card-link")

# print(address)
# print(price)
print(props_link)