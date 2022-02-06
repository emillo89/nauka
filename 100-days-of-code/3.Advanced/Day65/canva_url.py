import requests
from flask import Flask
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

URL="https://www.canva.com/design/DAE3gCjRUkI/4i80YVZnmPKakfol1YVEFA/view?utm_content=DAE3gCjRUkI&utm_campaign=designshare&utm_medium=link&utm_source=publishsharelink"
service = Service(executable_path="C:/Users/emils/PycharmProjects/Development/chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get(URL)

