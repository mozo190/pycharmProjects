import os
import re

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

sheet_research_link = os.environ.get('RESEARCH_LINK')
zillow_link = os.environ.get('ZILLOW_ClONE')

response = requests.get(zillow_link)
yc_web_page = response.text
# print(yc_web_page)

soup = BeautifulSoup(yc_web_page, "html.parser")

# print(soup.prettify())
address = soup.find_all("address", {"data-test": "property-card-addr"})

# strip=True removes the white spaces
addresses = [a.getText(strip=True) for a in address]

price_elements = soup.find_all("span", {"data-test": "property-card-price"})


def trim_prices(price):
    match = re.search(r'(\d+(?:,\d{3})*)', price)
    if match:
        return price[:match.end()].strip()
    return price


prices = [trim_prices(p.getText(strip=True)) for p in price_elements]

props_link = soup.find_all("a", class_="property-card-link")
paths = [link['href'] for link in props_link]

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(sheet_research_link)

# fill in the form
for i in range(len(addresses)):
    driver.get(sheet_research_link)
    address_input = driver.find_element(By.XPATH,
                                        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    address_input.clear()
    address_input.send_keys(addresses[i])

    price_input = driver.find_element(By.XPATH,
                                      '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_input.clear()
    price_input.send_keys(prices[i])

    link_input = driver.find_element(By.XPATH,
                                     '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_input.clear()
    link_input.send_keys(paths[i])

    submit_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    submit_button.click()

    driver.implicitly_wait(5)
