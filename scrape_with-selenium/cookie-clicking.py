from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, "cookie")
cookie.click()

# Get the cookie count
cookie_count = driver.find_element(By.ID, "money")
cookie_count_text = cookie_count.text
cookie_count_value = int(cookie_count_text.split(" ")[0])

# Get the upgrade items
items = driver.find_elements(By.CSS_SELECTOR, "#store div")
item_ids = [item.get_attribute("id") for item in items]

# Create a dictionary of the items and their prices
item_prices = [int(item.text.split("-")[1].strip().replace(",", "")) for item in items]
store_items = {}

for item in range(len(item_prices)):
    store_items[item_ids[item]] = item_prices[item]

# Buy the most expensive item
while True:
    for item in store_items:
        if cookie_count_value >= store_items[item]:
            driver.find_element(By.ID, item).click()
            break

    # Get the cookie count again
    cookie_count = driver.find_element(By.ID, "money")
    cookie_count_text = cookie_count.text
    cookie_count_value = int(cookie_count_text.split(" ")[0])

# driver.quit()
