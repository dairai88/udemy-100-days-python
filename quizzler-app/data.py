"""question data"""
import requests

params = {
    "amount": 10,
    "type": "boolean"
}

response = requests.get(url="https://opentdb.com/api.php", params=params, timeout=10)
response.raise_for_status()

data = response.json()
question_data = data["results"]
