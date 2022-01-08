import os
import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

CHROME_DRIVER_PATX = "C:/Users/emils/PycharmProjects/Development/chromedriver.exe"
SIMILAR_ACCOUNT = "chefsteps"
INSTAGRAM_EMAIL = os.environ["MY_EMAIL"]
INSTAGRAM_PASSWORD = os.environ["MY_PASSWORD"]

class InstaFollower:

    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(executable_path=driver_path)

    def login(self):
        URL = "https://www.instagram.com/"
        self.driver.get(URL)
        time.sleep(2)
        username = self.driver.find_element(By.NAME, "username")
        username.send_keys(INSTAGRAM_EMAIL)
        time.sleep(1)
        password = self.driver.find_element(By.NAME, "password")
        password.send_keys(INSTAGRAM_PASSWORD)
        time.sleep(2)
        password.send_keys(Keys.ENTER)
        time.sleep(2)
        not_save = self.driver.find_element(By.XPATH, "//*[@id='react-root']/section/main/div/div/div/div/button")
        not_save.click()
        time.sleep(2)
        notification = self.driver.find_element(By.XPATH, "/html/body/div[6]/div/div/div/div[3]/button[2]")
        notification.click()


    def find_followers(self):
        pass

    def follow(self):
        pass

insta = InstaFollower(CHROME_DRIVER_PATX)
insta.login()
insta.find_followers()
insta.follow()