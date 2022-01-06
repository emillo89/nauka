import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os


MY_EMAIL = os.environ["MY_EMAIL"]
MY_PASSWORD = os.environ["MY_PASSWORD"]

service = Service(executable_path="C:/Users/emils/PycharmProjects/Development/chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2Ca%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")

"""Sign in"""
sign_in = driver.find_element(By.PARTIAL_LINK_TEXT, "Zaloguj się")
sign_in.click()

#wait for few seconds
time.sleep(1)

email = driver.find_element(By.CSS_SELECTOR, "#username")
email.send_keys(MY_EMAIL)
password = driver.find_element(By.CSS_SELECTOR, "#password")
password.send_keys(MY_PASSWORD)
password.send_keys(Keys.ENTER)



