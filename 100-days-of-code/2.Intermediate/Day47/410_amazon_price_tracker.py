import requests
from bs4 import BeautifulSoup
import lxml
import smtplib
import os

my_email = os.environ["MY_EMAIL"]
password = os.environ["MY_PASSWORD"]

URL = "https://www.amazon.com/Instant-Pot-Plus-60-Programmable/dp/B01NBKTPTS/ref=psdc_3117954011_t2_B07W55DDFB"
ACCEPT_LANGUAGE = "pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7"
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36 OPR/82.0.4227.33"

headers = {
    'Accept-Language' : ACCEPT_LANGUAGE,
    'User-Agent': USER_AGENT
}

response = requests.get(url=URL, headers=headers)
content = response.text

soup = BeautifulSoup(content, "lxml")
title_product = soup.find(id="productTitle").getText().split(",")[0]
print(title_product)
your_occasion = soup.find(class_="a-size-medium a-color-price").getText()
price = float(your_occasion.split("$")[1])
print(price)

BUY_PRICE = 200

if price < BUY_PRICE:
    message = f"{title_product} is now ${price}"
    with smtplib.SMTP("smtp.gmail.com", port=587) as conenction:
        conenction.starttls()
        conenction.login(user=my_email, password=password)
        conenction.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Subject:Amazon price Alert!\n\n{message}\n{URL}"
        )

