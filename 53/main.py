from audioop import add
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import requests
import time

BASE_URL = 'https://www.zillow.com/'
driver = webdriver.Chrome(ChromeDriverManager().install())

form_url = 'https://forms.gle/nScH1yJggTukvsKk9'
zillow_url = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"

headers = {
    "Accept-Language":"en-US,en;q=0.9",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36"
}

zillow_response = requests.get(zillow_url, headers=headers).text
soup = BeautifulSoup(zillow_response, "lxml")

address_output = soup.find_all(class_='list-card-addr')
price_output = soup.find_all(class_='list-card-price')
url_output = soup.find_all("a", class_ = 'list-card-link')

property_data = []
for address in address_output:
    address_text = address.text    
    if '|' not in address.text:
        address_text = address_text.replace(',', '|', 1)
    address_text = address_text.split("|")[1].lstrip()
    property_data.append(address_text)

prices = []
for price in price_output:
    price_text = price.text
    if '+' in price_text:
        price_text = price_text.split('+')[0]
    elif '/' in price_text:
        price_text = price_text.split('/')[0]
    prices.append(price_text)

urls = []
for prop_url in url_output:
    final_url = prop_url['href']
    if BASE_URL not in final_url:
        final_url = f"{BASE_URL}{prop_url['href']}"
    if final_url not in urls:
        urls.append(final_url)

iterable_range = range(1,len(property_data))

result = { k:v  for k,*v in zip(iterable_range, property_data,prices,urls)}

# driver.get(form_url)
counter = 1

for value_set in result:
    driver.get(form_url)
    time.sleep(2)
    address_field = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    address_field.send_keys(result[counter][0])

    price_field = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_field.send_keys(result[counter][1])

    link_field = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_field.send_keys(result[counter][2])

    submit_btn = driver.find_element(by=By.XPATH, value="//*[text()='Submit']")
    submit_btn.click()
    counter += 1