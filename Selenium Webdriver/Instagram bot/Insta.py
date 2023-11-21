import time
from selenium import webdriver
from selenium.common import ElementClickInterceptedException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

API = 'https://www.instagram.com/'
ACC = "chefsteps"
USERNAME = ''
PASSWORD = ''

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)


class InstaFollower:

    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get(API)
        self.driver.maximize_window()
        time.sleep(5)

        # ---> Credentials
        email = self.driver.find_element(By.NAME, 'text')
        email.send_keys(USERNAME)
        email.send_keys(Keys.ENTER)
        time.sleep(1)
        password = self.driver.find_element(By.NAME, 'password')
        password.send_keys(PASSWORD)
        time.sleep(2)
        password.send_keys(Keys.ENTER)
        time.sleep(5)

    def find_follower(self):
        time.sleep(3)
        self.driver.get(f'{API}/{ACC}')
        follower_accounts = self.driver.find_element(by="css selector", value='div._aano')
        for i in range(100):
            followers = self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight",
                                                   follower_accounts)
            time.sleep(2)

    def follow(self):
        buttons = self.driver.find_elements_by_css_selector("li button")
        for button in buttons:
            # try:
            #     button.click()
            #     time.sleep(1)
            # except ElementClickInterceptedException:
            #     cancel_button = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
            #     cancel_button.click()
            if button.text != "Following":
                button.click()
                time.sleep(2)

    def close_browser(self):
        self.driver.quit()
        print("Done with it")


if __name__ == "__main__":
    insta_bot = InstaFollower()
    insta_bot.login()
    insta_bot.close_browser()
