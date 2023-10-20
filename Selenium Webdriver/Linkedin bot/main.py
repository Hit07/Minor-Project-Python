import time
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

ACCOUNT_EMAIL = ''
ACCOUNT_PASSWORD = ''
PHONE = "3517181912"

API = (
    "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491"
    "&keywords=python%20developer"
    "&location=London%2C%20England%2C%20United%20Kingdom"
    "&redirect=false&position=1&pageNum=0"
)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome()
driver.get(API)

# Click on sign-in button
time.sleep(3)
driver.find_element(By.LINK_TEXT, value="Sign in").click()

# Login
email = driver.find_element(By.NAME, 'session_key')
email.send_keys('hiteshnovember@gmail.com')
password = driver.find_element(By.NAME, 'session_password')
password.send_keys('Hitesh@7112001')
password.send_keys(Keys.ENTER)

# Confirmation By entering something that verification is complete
input("Have you completed:")

# apply button
time.sleep(3)
apply_button = driver.find_element(By.CSS_SELECTOR, value=".jobs-s-apply button")
apply_button.click()

time.sleep(2)
next_button = driver.find_element(By.CSS_SELECTOR, value='.ph5 pv4 button')
next_button.click()

driver.quit()
