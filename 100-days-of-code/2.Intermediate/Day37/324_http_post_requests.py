import requests
from datetime import datetime

USERNAME = "your_name"
TOKEN = "your_password"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)


#Created graph
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers= {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config,headers=headers)
# print(response.text)

"""https: // pixe.la / v1 / users / a - know / graphs / test - graph
a-know = USERNAME, test-graph = graphs1
https://pixe.la/v1/users/emillo89/graphs/graph1.html
"""

# today = datetime.now()
today = datetime(year=2021, month=12, day=6)

#Post piece of data
post_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "14.23"
}
# post_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
# response = requests.post(url=post_endpoint, json=post_data, headers=headers)
# print(response.text)

# Update - put
update_data = {
    "quantity": "15"
}

# update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
# update_response = requests.put(url=update_endpoint, json=update_data, headers=headers)
# print(update_response.text)

#Delete a pixel

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
delete_pixel = requests.delete(url=delete_endpoint,headers=headers)
print(delete_pixel.text)