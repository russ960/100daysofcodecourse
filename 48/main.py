from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

chrome_driver_path = "C:\dev\playground\100DaysOfCodePython_Udemy\chromedriver.exe"
driver = webdriver.Chrome(ChromeDriverManager().install())

url = "https://www.python.org/"
driver.get(url)

elements = driver.find_elements(By.XPATH, '//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li')

counter = 0
event_dict = {}
for attr in elements:
    split_attr = attr.text.split('\n')
    attr_dict = {}
    attr_dict['time'] = split_attr[0]
    attr_dict['name'] = split_attr[1]
    event_dict[counter] = attr_dict
    counter += 1

print(event_dict)
driver.quit()