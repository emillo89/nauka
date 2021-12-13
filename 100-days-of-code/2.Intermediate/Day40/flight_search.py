import requests
from flight_data import FlightData
import os

FLIGHT_ENDPOINT = "https://tequila-api.kiwi.com/locations/query"
API_KEY_FLIGHT = os.environ["API_KEY_FLIGHT"]


class FlightSearch:
    #This clas is responsible for talking to the Flight Search API
    def get_destination_code(self, city):
        #Find iataCode for a city
        headers = {
            "apikey": API_KEY_FLIGHT
        }
        params = {
            "term": city
        }
        response = requests.get(url=FLIGHT_ENDPOINT, headers=headers, params=params)
        code = response.json()["locations"][0]["code"]
        return code

    def check_flight(self, origin_city_code, destination_city_code, from_time, to_time):
        #Check the cheaper flight

        headers = {
            "apikey": API_KEY_FLIGHT
        }

        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }

        response = requests.get(url="https://tequila-api.kiwi.com/v2/search", headers=headers, params=query)
        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination_city_code}.")
            return None

        flight_data = FlightData(
            price=data["price"],
            city_code_from=data["route"][0]["cityCodeFrom"],
            city_code_to=data["route"][0]["cityCodeTo"],
            city_from=data["route"][0]["cityFrom"],
            city_to=data["route"][0]["cityTo"],
            utc_arrival=data["route"][0]["utc_arrival"].split("T"),
            utc_departure=data["route"][0]["utc_departure"].split("T")
        )

        print(f"{flight_data.city_to} : £{flight_data.price}")
        return flight_data
