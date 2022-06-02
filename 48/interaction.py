from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

chrome_driver_path = "C:\dev\playground\100DaysOfCodePython_Udemy\chromedriver.exe"
driver = webdriver.Chrome(ChromeDriverManager().install())
url = "https://en.wikipedia.org/wiki/Main_Page"
driver.get(url)

article_count = driver.find_element_by_css_selector("#articlecount a")
print(article_count.text)