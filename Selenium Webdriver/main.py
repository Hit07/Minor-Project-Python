from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By

API_ENDPOINT = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
# keep the browser open after the program terminates
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome()
driver.get("https://www.python.org")

# product_name = driver.find_element(By.ID, value="productTitle")
# price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_cent = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
#
# product_name_text = product_name.text.split(',')[0]
#
# print(f"{product_name_text}\nPrice:${price_dollar.text}.{price_cent.text}")

# search_bar = driver.find_element(By.NAME, "q")
# print(search_bar.get_property("role"))

# documentation_link = driver.find_element(By.CSS_SELECTOR, value=" .documentation-widget a")
# print(documentation_link.text)
#
# another_link = driver.find_element(By.XPATH, '//*[@id="container"]/li[3]/ul/li[1]/a')
# print(another_link.get_attribute("href"))  # link
# =======================================================================================================
# dates = []
# events = []
# for i in range(1, 6):
#     # Dates
#     date_element = driver.find_element(By.XPATH, f'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[{i}]/time')
#     dates.append(date_element.get_attribute('datetime').split('T')[0])
#     # Events
#     event_element = driver.find_element(By.XPATH, f'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[{i}]/a')
#     events.append(event_element.text)
#
# # list_event =  [{'Index': i,'Dates': date, 'Events': event} for i, (date, event) in enumerate(zip(dates, events))]
# list_event = [{'Dates': date, 'Events': event} for date, event in zip(dates, events)]
# list_event_dict = {i: event for i, event in enumerate(list_event)}

dates = driver.find_elements(By.CSS_SELECTOR,".event-widget a")
event = driver.find_elements(By.CSS_SELECTOR, ".event-widget a")
list_events = {}

for i in range(len(dates)):
    list_events[i] = {
        "Dates": dates[i].text,
        'Events': event[i].text
    }

print(list_events)
driver.close()
# driver.quit()
