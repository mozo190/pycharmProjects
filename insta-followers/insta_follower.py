import os
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class InstaFollower:
    def __init__(self):
        self.insta = os.environ.get('INSTA')
        self.insta_password = os.environ.get('INSTA_PASS')
        self.insta_name = os.environ.get('INSTA_NAME')
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.instagram.com/')
        sleep(2)
        cookies = self.driver.find_element(By.XPATH,
                                           '/html/body/div[4]/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[1]')  # Accept cookies
        cookies.click()
        sleep(2)

    def login(self):
        # login_button = self.driver.find_element(By.XPATH,
        #                                        '//*[@id="loginForm"]/div/div[3]/button/div')
        # login_button.click()

        sleep(2)
        email_input = self.driver.find_element(By.NAME, 'username')
        password_input = self.driver.find_element(By.NAME, 'password')
        email_input.send_keys(self.insta_name)
        password_input.send_keys(self.insta_password)
        submit_button = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')
        submit_button.click()
        sleep(5)
