import requests
from math import *
from twilio.rest import Client
import os

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = ""
NEWS_API_KEY = ""

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}

TWILIO_SID = ""
TWILIO_AUTH_TOKEN = ""

# Get yesterday's closing stock price.
response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for time, value in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print(yesterday_closing_price)

#Get the day before yesterday's closing stock price.
day_before_yesterday = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday["4. close"]
print(day_before_yesterday_closing_price)

#Substract between 1 and 2
substract = floor(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))
print(substract)
upd_down = None
if substract > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

#Percentage difference in price between closing price yesterday and closing price the day before yesterday.
sub_percent = round(substract/float(yesterday_closing_price) * 100, 2)
print(f"{sub_percent}%")

#If percentage is greater than 5 then use the News API to get articles related to the COMPANY_NAME.
news_param = {
    "apiKey": NEWS_API_KEY,
    "qInTitle": COMPANY_NAME
}

if abs(sub_percent) > 5:
    news_response = requests.get(NEWS_ENDPOINT, params=news_param)
    news_data = news_response.json()["articles"]
    # print(news_data)
    #Use Python slice operator to create a list that contains the first 3 articles
    three_article = news_data[:3]
    print(three_article)
    #List of the first 3 article's headline and description
    three_article_list = [f"{STOCK_NAME} : {up_down} : {sub_percent}%\nHeadline {article['title']}.\nBrief: {article['description']}" for article in three_article]
    print(three_article_list)

    # account_sid = os.environ[TWILIO_SID]
    # auth_token = os.environ[TWILIO_AUTH_TOKEN]
    #Send each article as a separate message via Twilio.
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    for article in three_article_list:
        message = client.messages.create(
            body=article,
            from_=+14092152435,
            to=+48514366497
        )
        print(message.status)

#Optional TODO: Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

