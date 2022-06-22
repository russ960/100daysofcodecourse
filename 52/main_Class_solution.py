from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
import time
import creds

#CHROME_DRIVER_PATH = YOUR CHROM DRIVER PATH
SIMILAR_ACCOUNT = creds.FOLLOWACCOUNT
USERNAME = creds.USERNAME
PASSWORD = creds.PASSWORD


class InstaFollower:

    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(5)

        username = self.driver.find_element_by_name("username")
        password = self.driver.find_element_by_name("password")

        username.send_keys(USERNAME)
        password.send_keys(PASSWORD)

        time.sleep(2)
        password.send_keys(Keys.ENTER)

    def find_followers(self):
        time.sleep(5)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}")

        time.sleep(4)
        followers = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers.click()

        time.sleep(2)
        modal = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]')
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        all_buttons = self.driver.find_elements_by_css_selector("li button")
        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()


bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()
