import requests

parameteres ={
    "amount": 10,
    "type": "boolean"
}

response = requests.get("https://opentdb.com/api.php?amount=10&type=boolean", params=parameteres)
response.raise_for_status()
question_data = response.json()["results"]
print(question_data)
