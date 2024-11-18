"""habit tracker"""
from datetime import datetime
import requests

USER_NAME = "sundalei"
TOKEN = "oarnud9I*test1234"
GROUP_ID = "graph1"

user_data = {
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

PIXELA_ENDPOINT = "https://pixe.la/v1/users"

# response = requests.post(url=PIXELA_ENDPOINT, json=user_data, timeout=20)
GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USER_NAME}/graphs"

graph_config = {
    "id": GROUP_ID,
    "name": "Reading Graph",
    "unit": "minute",
    "type": "int",
    "color": "shibafu",
    "timezone": "Asia/Shanghai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=GRAPH_ENDPOINT, timeout=20, json=graph_config, headers=headers)
# print(response.text)

PIXEL_CREATION_ENDPOINT = f"{PIXELA_ENDPOINT}/{USER_NAME}/graphs/{GROUP_ID}"

today = datetime(year=2024, month=11, day=17)
print(today.strftime("%Y%m%d"))

PIXEL_DATA = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "49"
}

# response = requests.post(url=PIXEL_CREATION_ENDPOINT, json=PIXEL_DATA, headers=headers, timeout=120)
# print(response.text)

UPDATE_ENDPOINT = f"{PIXELA_ENDPOINT}/{USER_NAME}/graphs/{GROUP_ID}/{today.strftime('%Y%m%d')}"

NEW_PIXEL_DATA = {
    "quantity": "14"
}

# response = requests.put(url=UPDATE_ENDPOINT, json=NEW_PIXEL_DATA, headers=headers, timeout=120)
# print(response.text)

DELETE_ENDPOINT = f"{PIXELA_ENDPOINT}/{USER_NAME}/graphs/{GROUP_ID}/20241118"

response = requests.delete(url=DELETE_ENDPOINT, headers=headers, timeout=120)
print(response.text)
