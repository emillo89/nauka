import requests
import os

USERS_ENDPOINT = os.environ["USERS_ENDPOINT"]


class DataUsers:

    def update_users(self, first_name, last_name, email):
        new_data = {
            "user": {
                "firstName": first_name,
                "lastName": last_name,
                "email": email

            }
        }
        response = requests.post(url=USERS_ENDPOINT, json=new_data)