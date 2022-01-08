import os
from selenium import webdriver


PROMISED_DOWN = 150
PRIMISED_UP = 10
CHROME_DRIVER_PATX = "C:/Users/emils/PycharmProjects/Development/chromedriver.exe"
TWITTER_EMAIL = os.environ["TWITTER_EMAIL"]
TWITTER_PASSWORD = os.environ["TWITTER_PASSWORD"]


class InternetSpeedTwitterBot:

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATX)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        pass

    def tweet_at_provider(self):
        pass