from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common import keys
import time

chrome_driver_path = "C:\dev\playground\100DaysOfCodePython_Udemy\chromedriver.exe"
driver = webdriver.Chrome(ChromeDriverManager().install())
url = "http://secure-retreat-92358.herokuapp.com/"
driver.get(url)

fname_input = driver.find_element_by_name('fName')
fname_input.send_keys("Russell") 

lname_input = driver.find_element_by_name('lName')
lname_input.send_keys("Johnson")

email_input = driver.find_element_by_name('email')
email_input.send_keys("russ@email.com")

submit_button = driver.find_element_by_css_selector('button')
time.sleep(2)
submit_button.click()


time.sleep(10)