import time
from selenium import webdriver
from selenium.webdriver.common.by import By

API = 'https://www.google.com/search?q=internet+speed&oq=in&gs_lcrp' \
      '=EgZjaHJvbWUqCwgAEEUYJxg7GIoFMgsIABBFGCcYOxiKBTIGCAEQRRg5MgYIAhBFGDsyBggDEEUYOzIJCAQQIxgnGIoFMg0IBRAAGIMBGLEDGIAEMg0IBhAuGIMBGLEDGIAEMgoIBxAAGLEDGIAEMg0ICBAAGIMBGLEDGIoFMg0ICRAAGIMBGLEDGIAE0gEJMjE1M2owajE1qAIAsAIA&sourceid=chrome&ie=UTF-8'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)


class InternetSpeed:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.down = 0
        self.up = 0

    # ---> gets internet speed from the google "Internet Speed"

    def get_internet_speed(self):
        self.driver.get(API)
        self.driver.maximize_window()
        time.sleep(4)
        run_button = self.driver.find_element(By.XPATH, '//*[@id="knowledge-verticals-internetspeedtest__test_button"]')
        run_button.click()
        time.sleep(20)
        while True:
            try:
                self.up = float(self.driver.find_element(By.XPATH, '//*[@id="knowledge-verticals'
                                                                   '-internetspeedtest__download"]/p[1]').text)
                self.down = float(self.driver.find_element(By.XPATH, '//*[@id="knowledge-verticals'
                                                                     '-internetspeedtest__upload"]/p[1]').text)
            except:
                time.sleep(3)
            else:
                break

        self.driver.quit()
