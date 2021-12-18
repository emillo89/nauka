import os
from twilio.rest import Client
import smtplib

ACCOUNT_SID_TWILIO = os.environ["ACCOUNT_SID_TWILIO"]
AUTH_TOKEN_TWILIO = os.environ["AUTH_TOKEN_TWILIO"]
PHONE_NUMBER = os.environ["PHONE_NUMBER"]
MY_PHONE = os.environ["MY_PHONE"]
MY_EMAIL = os.environ["MY_EMAIL"]
MY_PASSWORD = os.environ["MY_PASSWORD"]


class NotificationManager:

    def __init__(self):
        self.client = Client(ACCOUNT_SID_TWILIO, AUTH_TOKEN_TWILIO)

    def send_sms(self, message):
        #Message with cheaper flight
        message = self.client.messages.create(
            body=message,
            from_=PHONE_NUMBER,
            to=MY_PHONE
        )
        #Print if successfully sent
        print(message.sid)

    def send_emails(self,emails, message,google_flight_link):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            for email in emails:
                connection.sendmail(from_addr=MY_EMAIL,
                                    to_addrs=email,
                                    msg=f"Subject:Now Price Flight\n\n {google_flight_link.encode('UTF-8')}.")