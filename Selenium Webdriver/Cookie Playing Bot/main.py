from selenium import webdriver
from selenium.webdriver.common.by import By
from time import time


def get_upgrade_prices(driver):
    all_prices = driver.find_elements(By.CSS_SELECTOR, '#store b')
    item_prices = [int(price.text.split('-')[1].strip().replace(',', '')) for price in all_prices if price.text]
    return item_prices


def get_cookie_count(driver):
    money_element = driver.find_element(By.ID, 'money').text.replace(',', '')
    return int(money_element)


def find_affordable_upgrades(cookie_count, cookie_upgrades):
    affordable_upgrades = {cost: id for cost, id in cookie_upgrades.items() if cookie_count > cost}
    return affordable_upgrades


# Main function

def main():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option('detach', True)

    driver = webdriver.Chrome(options=chrome_options)
    driver.get('http://orteil.dashnet.org/experiments/cookie/')

    cookie = driver.find_element(By.ID, 'cookie')

    items = driver.find_elements(By.CSS_SELECTOR, '#store div')
    item_ids = [item.get_attribute('id') for item in items]

    time_out = time() + 5
    one_min = time() + 60  # 1 minutes

    while True:
        cookie.click()

        if time() > time_out:
            item_prices = get_upgrade_prices(driver)
            cookie_upgrades = dict(zip(item_prices, item_ids))
            cookie_count = get_cookie_count(driver)

            affordable_upgrades = find_affordable_upgrades(cookie_count, cookie_upgrades)

            if affordable_upgrades:
                highest_price_affordable_upgrade = max(affordable_upgrades)
                to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]
                driver.find_element(By.ID, to_purchase_id).click()

            time_out = time() + 5

        # time out if the time greater than 1 min
        if time() > one_min:
            cookie_per_s = driver.find_element(By.ID, 'cps').text
            print(cookie_per_s)
            break


if __name__ == "__main__":
    main()
