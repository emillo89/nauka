import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os

FB_PASSWORD = os.environ["FB_PASSWORD"]
FB_EMAIL = os.environ["FB_EMAIL"]

service = Service(executable_path="C:/Users/emils/PycharmProjects/Development/chromedriver.exe")
driver = webdriver.Chrome(service=service)


driver.get("https://tinder.com/")

time.sleep(1)

sign_in = driver.find_element(By.XPATH, "//*[@id='s-138260025']/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/span")
sign_in.click()

time.sleep(2)
sign_with_fb = driver.find_element(By.XPATH, "//*[@id='s-1866641101']/div/div/div[1]/div/div[3]/span/div[2]/button/span[2]")
sign_with_fb.click()

time.sleep(2)
# Switch to Facebookm login window
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

time.sleep(3)
#full path I use
cookie = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div/div/div/div[3]/button[2]")
cookie.click()

time.sleep(2)
fb_email = driver.find_element(By.XPATH, "/html/body/div/div[2]/div[1]/form/div/div[1]/div/input")
fb_email.send_keys(FB_EMAIL)
time.sleep(2)
fb_password = driver.find_element(By.XPATH, "/html/body/div/div[2]/div[1]/form/div/div[2]/div/input")
fb_password.send_keys(FB_PASSWORD)
fb_password.send_keys(Keys.ENTER)

#Switch back to Tinder window
driver.switch_to.window(base_window)
print(driver.title)


