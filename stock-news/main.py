"""stock news"""
import os
import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API_KEY = "EVFE4746MB9PVQ66"

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = "593525ea7c4a455d886f35a9e37e1551"

account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}

response = requests.get(url=STOCK_ENDPOINT, params=stock_params, timeout=10)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print(yesterday_closing_price)

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
print(day_before_yesterday_closing_price)

difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

print(difference)

diff_percent = round((abs(difference) / float(yesterday_closing_price)) * 100)
print(diff_percent)

if diff_percent > 5:
    news_param = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME
    }

    news_response = requests.get(url=NEWS_ENDPOINT, params=news_param, timeout=60)
    articles = news_response.json()["articles"]

    three_articles = articles[:3]

    formatted_articles = [f"{STOCK_NAME}: {up_down}{diff_percent}%\nHeadline: {article['title']}.\nBrief: {article['description']}"
      for article in three_articles]

    print(f"{account_sid}, {auth_token}")
    client = Client(account_sid, auth_token)

    for formatted_article in formatted_articles:
        message = client.messages.create(
        body=formatted_article,
        from_="whatsapp:+14155238886",
        to="whatsapp:+8618702152563")
        print(message.status)

    print("Get News")
