import os
import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

MY_EMAIL = os.environ["MY_EMAIL"]
MY_PASSWORD = os.environ["MY_PASSWORD"]
URL_ZILLOW = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22map" \
             "Bounds%22%3A%7B%22west%22%3A-122.94839873266822%2C%22east%22%3A-121.5023232932151%2C%22south%22%3A37." \
             "57406645355783%2C%22north%22%3A38.34498230666411%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A" \
             "%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value" \
             "%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%" \
             "3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse" \
             "%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isList" \
             "Visible%22%3Atrue%7D"

headers = {
    "Accept-Language": "pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 OPR/82.0.4227.43"

}

response = requests.get(url=URL_ZILLOW, headers=headers)
web_zillow = response.text

soup = BeautifulSoup(web_zillow, "html.parser")

#price
all_price_element = soup.find_all(name="div", class_="list-card-price")
all_price = [price.getText().split("/")[0].split('+')[0] for price in all_price_element]
# print(all_price)

#links
all_links_element = soup.select(selector=".list-card-info a")
all_links = []

for link in all_links_element:
    href = link["href"]
    if "https" not in href:
        all_links.append(f"https://www.zillow.com{href}")
    else:
        all_links.append(href)


#address
all_address_elements = soup.select(selector=".list-card-info address")
all_address = [address.text.split('|')[0] for address in all_address_elements]
# print(all_address)


#Use sellenium
chrome_driver_path = "C:/Users/emils/PycharmProjects/Development/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
GOOGLE_FORM_LINK = "https://docs.google.com/forms/d/e/1FAIpQLSe7cl6KgcA53XpXjmeFg_" \
                   "SBlBBzwMV09xH04lcNpt6j2ygITw/viewform?usp=sf_link"
#

driver.get(GOOGLE_FORM_LINK)
time.sleep(1)

#If you have to use your email and password
# email = driver.find_element(By.XPATH, "//*[@id='identifierId']")
# email.send_keys(MY_EMAIL)
# email.send_keys(Keys.ENTER)
# time.sleep(1)
# password = driver.find_element(By.XPATH, "//*[@id='password']/div[1]/div/div[1]/input")
# password.send_keys(MY_PASSWORD)
# password.send_keys(Keys.ENTER)

time.sleep(5)
for item in range(len(all_links)):
    address = driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/"
                                            "div/div[1]/input")
    time.sleep(3)
    price = driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/"
                                          "div[1]/input")
    link = driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/"
                                         "div[1]/input")
    address.send_keys(all_address[item])
    time.sleep(2)
    price.send_keys(all_price[item])
    time.sleep(2)
    link.send_keys(all_links[item])
    submit = driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[3]/div[1]/div[1]/div/span")
    submit.click()
    time.sleep(2)
    if item < len(all_price) - 1:
        next = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div[4]/a")
        next.click()
        time.sleep(2)
    else:
        driver.quit()
