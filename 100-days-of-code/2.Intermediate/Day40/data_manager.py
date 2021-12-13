import requests

SHEET_ENDPOINTS = "https://api.sheety.co/7bffeb9d054d88962d679acc00c1ebe5/flightDeals/prices"


class DataManager:

    def __init__(self):
        self.destination = {}

    def get_destination(self):
        #Loading data
        response = requests.get(url=SHEET_ENDPOINTS)
        data = response.json()
        self.destination = data["prices"]
        return self.destination

    def update_destination_code(self):
        #Updating row your data
        for row in self.destination:
            new_data = {
                "price": {
                    "iataCode": row["iataCode"]
                }
            }
            response = requests.put(url=f"{SHEET_ENDPOINTS}/{row['id']}", json=new_data)

