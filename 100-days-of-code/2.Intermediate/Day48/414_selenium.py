from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path="C:/Users/emils/PycharmProjects/Development/chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://www.python.org/")
# driver.get("https://www.amazon.com/Instant-Pot-Plus-60-Programmable/dp/B01NBKTPTS/ref=psdc_3117954011_t2_B07W55DDFB")

#search By.CLASS_NAME
logo_size = driver.find_element(By.CLASS_NAME, "python-logo" )
print(logo_size.size)

#search By.ID
button_info = driver.find_element(By.ID, "submit")
print(button_info.text)

#search By.NAME
button_info_2 = driver.find_element(By.NAME, "submit")
print(button_info_2.text)
print(button_info_2.tag_name)
print(button_info_2.get_attribute("name"))

#search By.CSS_Selector
documentation_link = driver.find_element(By.CSS_SELECTOR, ".jobs-widget a")
print(documentation_link.text)

#search By.PATH
bug_link = driver.find_element(By.XPATH, '//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(bug_link.text)
# driver.close()
driver.quit()