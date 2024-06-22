import os
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class InstaFollower:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--incognito')
        chrome_options.add_experimental_option("detach", True)
        self.insta = os.environ.get('INSTA')
        self.insta_password = os.environ.get('INSTA_PASS')
        self.insta_name = os.environ.get('INSTA_NAME')
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get('https://www.instagram.com/')
        sleep(2)
        cookies = self.driver.find_element(By.XPATH,
                                           '/html/body/div[4]/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[1]')  # Accept cookies
        cookies.click()
        sleep(2)

    def login(self):
        sleep(2)
        email_input = self.driver.find_element(By.NAME, 'username')
        password_input = self.driver.find_element(By.NAME, 'password')
        email_input.send_keys(self.insta_name)
        password_input.send_keys(self.insta_password)
        submit_button = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')
        submit_button.click()
        sleep(5)

        not_now = self.driver.find_element(By.XPATH, '//*[@id="mount_0_0_g4"]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div')
        if not_now:
            not_now.click()
        sleep(2)

    def find_followers(self):
        sleep(2)
        self.driver.get(f'https://www.instagram.com/{self.insta}')
        sleep(2)
        followers = self.driver.find_element(By.XPATH,
                                             '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers.click()
        sleep(2)

    def follow(self):
        pass
