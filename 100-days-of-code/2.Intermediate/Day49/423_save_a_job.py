import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os

MY_EMAIL = os.environ["MY_EMAIL"]
MY_PASSWORD = os.environ["MY_PASSWORD"]
PHONE_NUMBER = 123456778

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

time.sleep(1)

application = driver.find_element(By.CSS_SELECTOR, ".jobs-apply-button")
application.click()

phone = driver.find_element(By.CSS_SELECTOR, ".fb-single-line-text input")
if phone.text == "":
    phone.send_keys(PHONE_NUMBER)

# save = driver.find_element(By.XPATH, "/html/body/div[7]/div[3]/div[3]/div[2]/div/section[2]/div/div/div[1]/div/div[1]/div/div[2]/div[3]/div/button")
# save.click()



