from time import sleep
from selenium import webdriver
from selenium.common import ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

API = 'https://tinder.com/'
EMAIL = 'unknown.hitman.463@gmail.com'
PASSWORD = 'Hitesh@007'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome()
driver.get(API)

main_window = driver.window_handles[0]
driver.maximize_window()
sleep(4)
# Clicks on Login
login = driver.find_element(By.LINK_TEXT, 'Log in')
login.click()
sleep(3)

# Clicks on Facebook
try:
    fb = driver.find_element(By.XPATH,
                             '//*[@id="q1929195990"]/main/div/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button')
    fb.click()
    driver.maximize_window()
    fb_window = driver.window_handles[1]
    sleep(3)
except Exception as e:
    print(f"An error occurred: {e}")
    driver.refresh()
else:
    # ----------Switching to fb window
    driver.switch_to.window(fb_window)
    print(driver.title)
    sleep(5)

    # Find and interact with the email input field
    try:
        email_input = driver.find_element_by_name('email')
        # email_input.clear()
        email_input.send_keys(EMAIL)

        password_input = driver.find_element_by_name("pass")
        password_input.send_keys(PASSWORD)
        sleep(2)
        password_input.send_keys(Keys.ENTER)
    except Exception as e:
        print(f"An error occurred: {e}")
    else:
        # ------Switch back to Tinder window
        driver.switch_to.window(main_window)
        print(driver.title)

sleep(4)
'''Not working for me 
    Email and password is not been typed out hence no login
    Will try to come back'''
"""The below is the extension of solution to the project but I have not tried it"""

# Allow location
allow_location_button = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
allow_location_button.click()

# Disallow notifications
notifications_button = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
notifications_button.click()

# Allow cookies
cookies = driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button')
cookies.click()

# -----Standard mode in Tinder allows only 100 likes per day so the loop is set to 100
for n in range(100):

    # Add a one second delay between likes.
    sleep(1)
    count = 0

    try:
        print("called")
        like_button = driver.find_element_by_xpath(
            '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_button.click()

    # Catches the cases where there is a "Matched" pop-up in front of the "Like" button:
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element_by_css_selector(".itsAMatch a")
            match_popup.click()

        # Catches the cases where the "Like" button has not yet loaded
        except NoSuchElementException:
            sleep(4)
    else:
        count += 1
        print(count)

driver.quit()
