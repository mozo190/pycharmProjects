import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
from time import sleep

fb_email = os.environ.get('FB_EMAIL')
fb_password = os.environ.get('FB_PASSWORD')

driver = webdriver.Chrome()