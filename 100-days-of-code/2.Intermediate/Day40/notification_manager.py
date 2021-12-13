import os
from twilio.rest import Client

ACCOUNT_SID_TWILIO = os.environ["ACCOUNT_SID_TWILIO"]
AUTH_TOKEN_TWILIO = os.environ["AUTH_TOKEN_TWILIO"]
PHONE_NUMBER = os.environ["PHONE_NUMBER"]
MY_PHONE = os.environ["MY_PHONE"]


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