import requests
import random
import node
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

api_key = "your api"
account_sid = "your account"
auth_token = "your token"

parameters = {
    "lat": 50.717369,
    "lon": 23.252760,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get("https://api.openweathermap.org/data/2.5/onecall",params=parameters)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = True

for hour in weather_slice:
    condition_code = hour["weather"][0]["id"]
    if int(condition_code) > 800:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to snow today. REmeber to bring an ☂️.",
        from_='+14092152435',
        to='+48514366497'
    )
print(message.status)