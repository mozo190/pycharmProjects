from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep the browser open after the script is finished
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Open the website
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1")

price_dollar = driver.find_element(By.CLASS_NAME, "a-price-symbol")
price_amount = driver.find_element(By.CLASS_NAME, "a-price-whole")
price_cents = driver.find_element(By.CLASS_NAME, "a-price-fraction")
print(f"the price is {price_dollar.text}{price_amount.text}.{price_cents.text}")

# driver.close()  # Close the one tab browser
driver.quit()  # Close the whole browser
