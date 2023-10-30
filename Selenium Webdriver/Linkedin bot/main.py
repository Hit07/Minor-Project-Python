import time
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
email.send_keys('')
password = driver.find_element(By.NAME, 'session_password')
password.send_keys('')
password.send_keys(Keys.ENTER)

# Confirmation By entering something that verification is complete
input("Have you completed:")

# applied = driver.find_element(By.CLASS_NAME, 'job-card-container__footer-job-state')
# applied_text = applied.text
# if applied_text:
#     driver.refresh()
#     click_first = driver.find_element(By.CSS_SELECTOR,'.scaffold-layout__list-container li')
#     click_first.click()
#     print("success")

# list_of_jobs = driver.find_elements(By.CLASS_NAME,'scaffold-layout__list-container')
# for job in list_of_jobs:
#     print(job.text)
#     if applied_text:
#         pass


# apply button
time.sleep(3)
apply_button = driver.find_element(By.CSS_SELECTOR, value=".jobs-s-apply button")
apply_button.click()

time.sleep(3)
next_button = driver.find_element(By.CSS_SELECTOR, value=' .display-flex button')
next_button.click()
next_button_1 = driver.find_element(By.CLASS_NAME, 'artdeco-button--primary')
next_button_1.click()
review = driver.find_element(By.CLASS_NAME, 'artdeco-button--primary')
review.click()
submit_button = driver.find_element(By.CLASS_NAME, 'artdeco-button--primary')
submit_button.click()
time.sleep(3)


driver.quit()
