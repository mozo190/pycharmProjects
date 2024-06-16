from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep the browser open after the script is finished
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Open the website
driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1")
#
# price_dollar = driver.find_element(By.CLASS_NAME, "a-price-symbol")
# price_amount = driver.find_element(By.CLASS_NAME, "a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME, "a-price-fraction")
# print(f"the price is {price_dollar.text}{price_amount.text}.{price_cents.text}")

driver.get("https://www.python.org/")
# bug_link = driver.find_element(By.XPATH, '//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)
# bug_link.click()

dict_list = {}
for i in range(1, 6):
    date_ = driver.find_element(By.XPATH, f'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[{i}]/time')
    text_ = driver.find_element(By.XPATH, f'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[{i}]/a')
    dict_list[i] = {
        "time": date_.text,
        "name": text_.text
    }
print(dict_list)
# driver.close()  # Close the one tab browser
driver.quit()  # Close the whole browser
