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
