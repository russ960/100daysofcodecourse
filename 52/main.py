import creds
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
    
    def login(self):
        url = 'https://www.instagram.com/accounts/login/'
        self.driver.get(url)
        time.sleep(3)

        user_name_input = self.driver.find_element(by=By.NAME, value='username')
        user_name_input.send_keys(creds.USERNAME)

        password_input = self.driver.find_element(by=By.NAME, value='password')
        password_input.send_keys(creds.PASSWORD)

        login_button = self.driver.find_element(by=By.XPATH, value='//*[@id="loginForm"]/div/div[3]/button')
        login_button.click()

        time.sleep(3)
        save_login_not_now_button = self.driver.find_element(by=By.XPATH, value="//*[text()='Not Now']")
        save_login_not_now_button.click()
        time.sleep(4)
        notifications_not_now_button = self.driver.find_element(by=By.XPATH, value="//*[text()='Not Now']")
        notifications_not_now_button.click()

    def find_followers(self):
        url = "https://www.instagram.com/simpleprogrammer/"
        self.driver.get(url)
        time.sleep(5)
        followers_link = self.driver.find_element(by=By.XPATH, value="//*[text()=' followers']")
        followers_link.click()

        time.sleep(5)
        page = self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div[2]')
        for char in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", page)
            time.sleep(2)

    
    def follow(self):
        pass

insta_follow = InstaFollower()

insta_follow.login()
insta_follow.find_followers()
insta_follow.follow()