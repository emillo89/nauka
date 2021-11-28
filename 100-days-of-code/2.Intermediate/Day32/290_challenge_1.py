import datetime as dt
import smtplib
import random

my_email = "appbrewery5@gmail.com"
password = "testowe1234"

now = dt.datetime.now()
day = now.weekday()
if day == 6:
    with open("quotes.txt", "r") as file:
        text = file.readlines()
        quotes = random.choice(text)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=my_email,
                            msg=f"Subject:Monday Motivation\n\n {quotes}")
