import os
import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

PROMISED_DOWN = 30
PRIMISED_UP = 10
CHROME_DRIVER_PATX = "C:/Users/emils/PycharmProjects/Development/chromedriver.exe"
TWITTER_EMAIL = os.environ["TWITTER_EMAIL"]
TWITTER_USER = os.environ["TWITEER_USER"]
TWITTER_PASSWORD = os.environ["TWITTER_PASSWORD"]


class InternetSpeedTwitterBot:

    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.upload = 0
        self.download = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(1)
        notification = self.driver.find_element(By.XPATH, "//*[@id='_evidon-banner-acceptbutton']")
        notification.click()
        time.sleep(1)
        go = self.driver.find_element(By.CLASS_NAME, "start-text")
        go.click()
        time.sleep(40)
        download = self.driver.find_element(By.CLASS_NAME, "download-speed")
        upload = self.driver.find_element(By.CLASS_NAME, "upload-speed")
        self.download = download.text
        self.upload = upload.text

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/i/flow/login")
        time.sleep(1)
        email = self.driver.find_element(By.XPATH, "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/"
                                                   "div/div/div[2]/div[2]/div[1]/div/div[5]/label/div/div[2]/div/input")
        email.send_keys(TWITTER_EMAIL)
        time.sleep(1)
        email.send_keys(Keys.ENTER)
        time.sleep(1)
        user = self.driver.find_element(By.XPATH, "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/"
                                                  "div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input")
        user.send_keys(TWITTER_USER)
        time.sleep(1)
        user.send_keys(Keys.ENTER)
        time.sleep(2)
        password = self.driver.find_element(By.XPATH, "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/"
                                                      "div/div/div[2]/div[2]/div[1]/div/div[3]/div/label/div/div[2]/"
                                                      "div[1]/input")
        password.send_keys(TWITTER_PASSWORD)
        time.sleep(3)
        password.send_keys(Keys.ENTER)
        time.sleep(2)
        tweet_information = self.driver.find_element(By.XPATH, "//*[@id='react-root']/div/div/div[2]/main/div/div/"
                                                               "div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/"
                                                               "div[2]/div[1]/div/div/div/div/div/div/div/div/div/"
                                                               "label/"
                                                               "div[1]/div/div/div/div/div[2]/div/div/div/div")
        tweet = f"Hey Internet Provide, why is my internet speed {self.download} download / {self.upload}" \
                f" upload when I pay for {PROMISED_DOWN} download / {PRIMISED_UP} upload?"
        time.sleep(2)
        tweet_information.send_keys(tweet)
        time.sleep(1)
        tweet_button = self.driver.find_element(By.XPATH, "//*[@id='react-root']/div/div/"
                                                          "div[2]/main/div/div/div/div[1]/"
                                                          "div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/"
                                                          "div/div[2]/div[3]/div/span/span")
        tweet_button.click()


bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATX)
bot.get_internet_speed()
bot.tweet_at_provider()
