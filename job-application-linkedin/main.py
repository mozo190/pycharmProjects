import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

link_email = os.environ.get("MY_EMAIL")
link_password = os.environ.get("LINKEDIN_PASS")
phone = os.environ.get("PHONE")
url = ("https://www.linkedin.com/jobs/search/?currentJobId=3947629969&distance=25&f_AL=true&f_TPR="
       "r604800&geoId=106079947&keywords=python%20developer&origin="
       "JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&spellCorrectionEnabled=true")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(url)
button = driver.find_element(By.XPATH, '/html/body/div[3]/header/nav/div/a[2]')
button.click()

username = driver.find_element(By.ID, "username")
username.send_keys(link_email)

password = driver.find_element(By.ID, "password")
password.send_keys(link_password)

login_button = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')
login_button.click()

time.sleep(10)

jobs = driver.find_elements(By.CLASS_NAME, "jobs-search-results-list")
for job in jobs:
    job.click()
    time.sleep(5)
    try:
        apply = driver.find_element(By.ID, "ember367")
        apply.click()
        time.sleep(5)
        submit = driver.find_element(By.XPATH, '//*[@id="ember873"]')
        submit.click()
        time.sleep(5)
        review = driver.find_element(By.XPATH, '//*[@id="ember895"]')
        review.click()
        time.sleep(5)
        submit_application = driver.find_element(By.XPATH, '//*[@id="ember889"]')
    except Exception as e:
        print(e)
        continue
