import os
from time import sleep
from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

insta = os.environ.get('INSTA')
insta_password = os.environ.get('INSTA_PASSWORD')

driver = webdriver.Chrome()
driver.get('https://www.instagram.com/')

sleep(2)