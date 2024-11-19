"""workout tracker"""
from datetime import datetime
import json
import requests

with open(file="config.json", encoding="utf-8") as file:
    config = json.load(file)

APP_ID = config["APP_ID"]
API_KEY = config["API_KEY"]
HOST_DOMAIN = "https://trackapi.nutritionix.com"
ENDPOINT = "/v2/natural/exercise"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

body = {
    "query": input("Tell me which exercise you did: ")
}

response = requests.post(url=f"{HOST_DOMAIN}{ENDPOINT}", json=body, headers=headers, timeout=10)
workout_data = response.json()['exercises']
today = datetime.now()

SHEETY_ENDPOINT = 'https://api.sheety.co/eda831fe47412aff6d3eadd7d8b66bdb/workoutTracking/workouts'

WORKOUT_HEADER = {
    "Authorization": f"Basic {config["AUTH_TOKEN"]}"
}

for exercise in workout_data:
    print(exercise)
    WORKOUT_BODY = {
        "workout": {
            "date": f"{today.strftime("%d/%m/%Y")}",
            "time": f"{today.strftime("%H:%M:%S")}",
            "exercise": f"{exercise["name"].title()}",
            "duration": f"{exercise["duration_min"]}",
            "calories": f"{exercise["nf_calories"]}"
        }
    }
    workout_response = requests.post(
        url=SHEETY_ENDPOINT,
        json=WORKOUT_BODY,
        headers=WORKOUT_HEADER,
        timeout=20)
    print(workout_response.json())
