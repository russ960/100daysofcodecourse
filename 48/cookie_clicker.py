from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common import keys
import time

TIME_TO_RUN = 300

chrome_driver_path = "C:\dev\playground\100DaysOfCodePython_Udemy\chromedriver.exe"
driver = webdriver.Chrome(ChromeDriverManager().install())
url = "https://orteil.dashnet.org/experiments/cookie/"
driver.get(url)

cookie = driver.find_element(by=By.CSS_SELECTOR, value='div #cookie')

total_time_to_run = time.time() + TIME_TO_RUN
while time.time() < total_time_to_run:
    run_time = time.time() + 5
    while time.time() < run_time:
        cookie.click()

    store = driver.find_elements(by=By.CSS_SELECTOR, value='#store div b')
    store_items = [(item.text).rstrip().split('\n')[0].split(' - ') for item in store if item.text != '']


    unavailable_store = driver.find_elements(by=By.CSS_SELECTOR, value='#store .grayed')
    unavilable_items = [(item.text).rstrip().split('\n')[0].split(' - ') for item in unavailable_store if item.text != '']

    available_to_buy = []
    for store_item in store_items:
        if store_item not in unavilable_items:
            available_to_buy.append(store_item)
    if len(available_to_buy) > 0:
        item_to_buy = driver.find_element(by=By.ID, value=f"buy{available_to_buy[-1:][0][0]}")
        item_to_buy.click()
    
cookies_count = driver.find_element(by=By.ID, value='cps')
print(f"Cookies per second: {cookies_count.text}")
# print(store_items)
# print(unavilable_items)
# print(available_to_buy)
#time.sleep(10)