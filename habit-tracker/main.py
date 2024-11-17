"""habit tracker"""
import requests

USER_NAME = "sundalei"
TOKEN = "oarnud9I*test1234"

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
    "id": "graph1",
    "name": "Reading Graph",
    "unit": "minute",
    "type": "int",
    "color": "shibafu",
    "timezone": "Asia/Shanghai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

response = requests.post(url=GRAPH_ENDPOINT, timeout=20, json=graph_config, headers=headers)
print(response.text)
