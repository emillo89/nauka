import os
import time

from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

CHROME_DRIVER_PATX = "C:/Users/emils/PycharmProjects/Development/chromedriver.exe"
SIMILAR_ACCOUNT = "chefsteps"
INSTAGRAM_EMAIL = os.environ["MY_EMAIL"]
INSTAGRAM_PASSWORD = os.environ["MY_PASSWORD"]
URL = "https://www.instagram.com/"


class InstaFollower:

    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(executable_path=driver_path)

    def login(self):
        """Function takes your email, password and login on your account."""
        self.driver.get(URL)
        time.sleep(2)
        cookie = self.driver.find_element(By.XPATH, "/html/body/div[4]/div/div/button[1]")
        cookie.click()
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
        """Function find all followers in your choice location"""
        time.sleep(2)
        self.driver.get(f"{URL}{SIMILAR_ACCOUNT}/")
        followers = self.driver.find_element(By.XPATH, "//*[@id='react-root']/section/main/div/header/"
                                                       "section/ul/li[2]/a")
        followers.click()
        time.sleep(2)
        scroll_down = self.driver.find_element(By.XPATH, "/html/body/div[6]/div/div/div[2]")

        for i in range(2):
            self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', scroll_down)
            time.sleep(1)

    def follow(self):
        """Function adds all followers to your follows"""
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, "li div button")
        for button in all_buttons:
            try:
                button.click()
                time.sleep(2)

            except ElementClickInterceptedException:
                cancel = self.driver.find_element(By.XPATH, "/html/body/div[7]/div/div/div/div[3]/button[2]")
                cancel.click()
                time.sleep(1)


insta = InstaFollower(CHROME_DRIVER_PATX)
insta.login()
insta.find_followers()
insta.follow()
