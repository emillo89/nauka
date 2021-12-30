from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

service = Service(executable_path="C:/Users/emils/PycharmProjects/Development/chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

statistics = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# statistics.click()

all_portals = driver.find_element(By.PARTIAL_LINK_TEXT, "All portals")
# all_portals.click()

search = driver.find_element(By.NAME, "search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)