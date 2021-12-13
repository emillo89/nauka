import requests

SHEET_ENDPOINTS = "https://api.sheety.co/7911f45481e53f61eeaeeb89b6dafe76/flightDeals/users"
response = requests.get(url=SHEET_ENDPOINTS)
data = response.json()["users"]
print(data)