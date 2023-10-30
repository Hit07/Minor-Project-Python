from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


PROMISED_DOWN = 100
PROMISED_UP = 100
CHROME_DRIVER_PATH = ''
# 'https://twitter.com/i/flow/login'
TWITTER_EMAIL = 'unknown.hitman.463@gmail.com'
TWITTER_PASSWORD = 'Hitesh@007'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
s = Service(CHROME_DRIVER_PATH)
options = Options()
options.add_argument("start-maximized")


class InternetSpeedTwitterBot:

    def __init__(self, path):
        self.driver = webdriver.Chrome(service=s, options=options)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        pass

    def tweet_at_provider(self):
        pass


obj = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
obj.get_internet_speed()
obj.tweet_at_provider()
