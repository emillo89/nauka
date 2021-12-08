import requests
from datetime import datetime
import node
import os

GENDER = "male"
WEIGHT = 86
HEIGHT = 179
AGE = 32

exercise_text = input("Tell mew which exercise you did?: ")

ID = os.environ["API_ID"]
KEY = os.environ["API_KEY"]
endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

endpoint_params = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE

}

headers = {
    "x-app-id": ID,
    "x-app-key": KEY,
}

response = requests.post(url=endpoint, json=endpoint_params, headers=headers)
results = response.json()
print(results)
#
date = datetime.now()
print(date.strftime("%d/%m/%Y"))
print(date.strftime("%X"))


for exercise in results["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": date.strftime("%d/%m/%Y"),
            "time": date.strftime("%X"),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }

    }
"Autentication"

auth_sheety = {
    "Authorization": os.environ["Authorization"],

}

sheety_edpoints = "https://api.sheety.co/7bffeb9d054d88962d679acc00c1ebe5/emilWorkouts/workouts"

sheet_response = requests.post(url=sheety_edpoints, json=sheet_inputs, headers=auth_sheety)
print(sheet_response.json())
print(sheet_response.text)
