from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path="C:/Users/emils/PycharmProjects/Development/chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

statistics = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
print(statistics.text)