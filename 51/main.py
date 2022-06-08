from tracemalloc import start
import creds
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

PROMISED_DOWN = 50
PROMISED_UP = 2
TWITTER_EMAIL = creds.twitter_email
TWITTER_PASSWORD = creds.twitter_password


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        url = 'https://www.speedtest.net/'
        self.driver.get(url)

        start_button = self.driver.find_element(by=By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        start_button.click()

        time.sleep(60)
        self.down = float(self.driver.find_element_by_css_selector('.result-data-large.number.result-data-value.download-speed').text)
        self.up = float(self.driver.find_element_by_css_selector('.result-data-large.number.result-data-value.upload-speed').text)
        
        print(f"down: {self.down} \nup: {self.up}")

    def tweet_at_provider(self):
        url = 'https://twitter.com/login/'
        self.driver.get(url)
        time.sleep(3)

        username_login = self.driver.find_element(by=By.NAME, value='text')
        username_login.send_keys(creds.twitter_email)
        time.sleep(3)

        next_button = self.driver.find_element(by=By.XPATH, value="//*[text()='Next']")
        next_button.click()
        time.sleep(3)

        password_login = self.driver.find_element(by=By.NAME, value='password')
        password_login.send_keys(creds.twitter_password)
        time.sleep(5)

        login_button = self.driver.find_element(by=By.XPATH, value="//*[text()='Log in']")
        login_button.click()
        time.sleep(20)

        tweetbox = self.driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div')
        tweetbox.send_keys("Test message ignore.")

        tweet_button = self.driver.find_element(by=By.XPATH, value="//*[text()='Tweet']")
        tweet_button.click()

        time.sleep(10)
        self.driver.quit()


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()

if bot.down < PROMISED_DOWN or bot.up < PROMISED_UP:
    bot.tweet_at_provider()

    