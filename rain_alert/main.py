"""rain alert"""
import os
import requests
from twilio.rest import Client

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY = os.environ.get("OWM_API_KEY")
LAT = 31.230391
LON = 121.473701

account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")
client = Client(account_sid, auth_token)

params = {
    "lat": LAT,
    "lon": LON,
    "appid": API_KEY,
    "cnt": 4
}

response = requests.get(url=OWM_ENDPOINT, params=params, timeout=20)
response.raise_for_status()
weather_data = response.json()

will_rain = False  # pylint: disable=invalid-name
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True  # pylint: disable=invalid-name
if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="It's going to rain today. Remember to bring an ☂️",
        from_="whatsapp:+14155238886",
        to="whatsapp:+8618702152563")

    print(message.body)
