from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

service = Service(executable_path="C:/Users/emils/PycharmProjects/Development/chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("http://secure-retreat-92358.herokuapp.com/")


first_name = driver.find_element(By.NAME, "fName")
first_name.send_keys("Emil")
last_name = driver.find_element(By.NAME, "lName")
last_name.send_keys("S")
email_address = driver.find_element(By.NAME, "email")
email_address.send_keys("emils@cos.com")
button = driver.find_element(By.CLASS_NAME, "btn")
button.click()