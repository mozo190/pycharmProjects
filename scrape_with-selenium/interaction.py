from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

# articles = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]')
# print(articles.text)

search = driver.find_element(By.NAME, "search")
search.send_keys("Python", Keys.ENTER)


# driver.quit()
