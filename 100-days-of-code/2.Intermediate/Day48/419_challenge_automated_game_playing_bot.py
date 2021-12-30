from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service(executable_path="C:/Users/emils/PycharmProjects/Development/chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

#Get cookie to clik on.
cookie = driver.find_element(By.ID, "cookie")

#Get upgrade item ids
items = driver.find_elements(By.CSS_SELECTOR, "#store div")
items_ids = [item.get_attribute("id") for item in items]
print(items_ids)

timeout = time.time() + 5
five_min = time.time() + 3 * 5

while True:
    cookie.click()

    #Every 5 seconds
    if time.time() > timeout:

        #Get all upgrade b tags
        all_price = driver.find_elements(By.CSS_SELECTOR, "#store b")
        item_prices = []

        #Convert text into an another price
        for price in all_price:
            element_text = price.text
            if element_text != "":
                cost = int(element_text.split("-")[1].strip().replace(",",""))
                item_prices.append(cost)

        print(item_prices)
        #Create dictionary of store items and pieces
        cookie_upgrade = {}
        for n in range(len(item_prices)):
            cookie_upgrade[item_prices[n]] = items_ids[n]

        print(cookie_upgrade)

        #Get current cookie count
        money_element = driver.find_element(By.ID, "money").text
        print(money_element)
        cookie_count = int(money_element)

        #Find upgrade that we can currently afford
        affordable_upgrades = {}
        for cost, id in cookie_upgrade.items():
            if cookie_count > cost:
                affordable_upgrades[cost] = id

        #Purchase the most expensive affordable upgrade
        highest_price_affordable_upgrade = max(affordable_upgrades)
        print(highest_price_affordable_upgrade)
        to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]

        driver.find_element(By.ID, to_purchase_id).click()

        #Add another 5 seconds untill the next check
        timeout = time.time() + 5
    #After 5 minutes stop the bot and check the cookie per second count.
    if time.time() > five_min:
        cookie_per_s = driver.find_element(By.ID, "cps").text
        print(cookie_per_s)
        break


