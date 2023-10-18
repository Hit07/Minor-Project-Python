from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome()
driver.get('https://secure-retreat-92358.herokuapp.com/')
# ------------------------------------------------------------------------------------------------------------
# article_counts = driver.find_element(By.CSS_SELECTOR,'#articlecount a')
# # article_counts.click()
#
# encylo = driver.find_element(By.LINK_TEXT,"encyclopedia")
# # encylo.click()
# # print(article_counts.text.split(" ")[0])
# search_bar= driver.find_element(By.NAME,"search")
# search_bar.send_keys("Python")
# search_bar.send_keys(Keys.ENTER)
# ------------------------------------------------------------------------------------------------------------
list_attr = {'fName': 'Hitesh', 'lName': 'Narayana', 'email': "123@gmail.com"}

for key, value in list_attr.items():
    field_values = driver.find_element(By.NAME, key)
    field_values.send_keys(value)
    # field_values.send_keys(Keys.ENTER)

submit = driver.find_element(By.CSS_SELECTOR, 'form button')
submit.click()

driver.quit()
