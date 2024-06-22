import os
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

insta = os.environ.get('INSTA')
insta_password = os.environ.get('INSTA_PASS')
insta_name = os.environ.get('INSTA_NAME')

driver = webdriver.Chrome()
driver.get('https://www.instagram.com/')

sleep(2)
cookies = driver.find_element(By.XPATH, '/html/body/div[4]/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[1]')  # Accept cookies
cookies.click()

sleep(2)
