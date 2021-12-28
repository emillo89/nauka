import pandas
import datetime as dt
import random
import smtplib
import os

my_email = os.environ["MY_EMAIL"]
password = os.environ["MY_PASSWORD"]

# current day and month
today = dt.datetime.now()
today_tuple = (today.month, today.day)

# read pandas csv file
data = pandas.read_csv("birthdays.csv")
birthday_dict = {(row.month, row.day) : row for index, row in data.iterrows()}
if today_tuple in birthday_dict:
    number = random.randint(1, 3)
    birthday_person = birthday_dict[today_tuple]
    file_path = f"letter_templates/letter_{number}.txt"
    with open(file_path) as letter_file:
        content = letter_file.read()
        content = content.replace("[NAME]", birthday_person["name"])
    print(content)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=birthday_person["email"],
                            msg=f"Subject:Happy Birthday\n\n {content}")