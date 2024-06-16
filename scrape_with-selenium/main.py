from selenium import webdriver

# Keep the browser open after the script is finished
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Open the website
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")