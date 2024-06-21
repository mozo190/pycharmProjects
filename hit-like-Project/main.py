import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
from time import sleep

fb_email = os.environ.get('FB_EMAIL')
fb_password = os.environ.get('FB_PASSWORD')

driver = webdriver.Chrome()
driver.get('https://www.twitter.com/')

sleep(2)
login_button = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/a[2]')
login_button.click()

sleep(2)
base_window = driver.window_handles[0]  # Base window
fb_login_window = driver.window_handles[1]  # Login window
driver.switch_to.window(fb_login_window)
print(driver.title)

email = driver.find_element(By.XPATH, '//*[@id="email"]')
password = driver.find_element(By.XPATH, '//*[@id="pass"]')
email.send_keys(fb_email)
password.send_keys(fb_password)
password.send_keys(Keys.ENTER)

driver.switch_to.window(base_window)
print(driver.title)

sleep(5)

allow_location = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div/main/div/div/div/div/div/div[2]/div/div[2]/div/div/div/div/div/div[2]/div[2]/div[2]/div/div/div/div[2]/div/div/div/div')
allow_location.click()

notifications_button = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div/main/div/div/div/div/div/div[2]/div/div[2]/div/div/div/div/div/div[2]/div[2]/div[2]/div/div/div/div[2]/div/div/div/div')
notifications_button.click()

cookies = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div/main/div/div/div/div/div/div[2]/div/div[2]/div/div/div/div/div/div[2]/div[2]/div[2]/div/div/div/div[2]/div/div/div/div')
cookies.click()

