"""iss over head"""
from datetime import datetime
import smtplib
import time
import requests

MY_EMAIL = "sundalei2011@163.com"
APP_PASSWORD = "QDiGtwHSabLfLaTV"
MY_LAT = 31.230391
MY_LONG = 121.473701


def is_iss_overhead():
    """is iss overhead"""
    response = requests.get(url="http://api.open-notify.org/iss-now.json", timeout=10)
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.
    return MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5


def is_night():
    """is night"""
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
        "tzid": "Asia/Shanghai"
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters, timeout=10)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    return time_now >= sunset or time_now <= sunrise

while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        with smtplib.SMTP_SSL(host="smtp.163.com", port=465) as connection:
            connection.login(user=MY_EMAIL, password=APP_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg="Subject:Look Up👆\n\nThe ISS is above you in the sky.")
