"""day 33"""
from datetime import datetime
import requests

MY_LAT = 31.230391
MY_LONG = 121.473701

parameter = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
    "tzid": "Asia/Shanghai"
}

response = requests.get(url="https://api.sunrise-sunset.org/json", timeout=5, params=parameter)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

sunrise_dt = datetime.fromisoformat(sunrise)
sunset_dt = datetime.fromisoformat(sunset)

print(sunrise_dt.hour)
print(sunset_dt.hour)

time_now = datetime.now()

print(time_now)
