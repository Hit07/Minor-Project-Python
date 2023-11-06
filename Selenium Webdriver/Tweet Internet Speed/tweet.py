import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

API = 'https://twitter.com/login'

TWITTER_EMAIL = 'unknown.hitman.463@gmail.com'
TWITTER_PASSWORD = 'Hitesh@007'

PROMISED_DOWN = 100
PROMISED_UP = 100

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)


class Tweet:

    def __init__(self):
        self.driver = webdriver.Chrome()

    def tweet_at_provider(self,post):
        self.driver.get(API)
        self.driver.maximize_window()
        time.sleep(5)

        # ---> Credentials
        email = self.driver.find_element(By.NAME,'text')
        email.send_keys(TWITTER_EMAIL)
        email.send_keys(Keys.ENTER)
        time.sleep(1)
        password = self.driver.find_element(By.NAME,'password')
        password.send_keys(TWITTER_PASSWORD)
        time.sleep(2)
        password.send_keys(Keys.ENTER)
        time.sleep(5)

        # ----> Writing Message
        draft = self.driver.find_element(By.CSS_SELECTOR,'.DraftEditor-editorContainer div')
        draft.send_keys(post)
        time.sleep(3)

        # ---> Post button
        tweet_button = self.driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/div[3]')
        tweet_button.click()
        time.sleep(3)
        self.driver.quit()
