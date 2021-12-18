import requests
import os

USERS_ENDPOINT = os.environ["USERS_ENDPOINT"]


class DataUsers:

    def __init__(self):
        self.customer_data = {}

    def update_users(self, first_name, last_name, email):
        new_data = {
            "user": {
                "firstName": first_name,
                "lastName": last_name,
                "email": email

            }
        }
        response = requests.post(url=USERS_ENDPOINT, json=new_data)

    def get_customer_emails(self):
        response = requests.get(url=USERS_ENDPOINT)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data
