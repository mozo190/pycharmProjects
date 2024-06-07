import os

import requests
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()
alpha_vantage_api_key = os.getenv("ALPHA_VANTAGE_API_KEY")
news_api_key = os.getenv("NEWS_API_KEY")

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": "alpha_vantage_api_key"
}

response = requests.get(url=STOCK_ENDPOINT, params=parameters, headers={"Accept": "application/json"})
response.raise_for_status()
data = response.json()
# print(data)

news_response = requests.get(url=NEWS_ENDPOINT, params={"q": COMPANY_NAME, "apiKey": news_api_key})
news_response.raise_for_status()
news_data = news_response.json()
# print(news_data)

news_list = news_data["articles"]
# print(news_list)

data_list = [value for (key, value) in data["Time Series (Daily)"].items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
day_before = data_list[1]
day_before_closing_price = day_before["4. close"]
print(day_before_closing_price)
print(yesterday_closing_price)

difference = abs(float(yesterday_closing_price) - float(day_before_closing_price))
percentage = (difference / float(yesterday_closing_price)) * 100
print(f"{difference:.2f} a difference")
print(f"{percentage:.2f}% a percentage")

if percentage > 5:
    print("Get News")
    for news in news_list[:3]:
        print(news["title"])
        print(news["description"])
        print("\n")
        account_sid = os.getenv("TWILIO_ACCOUNT_SID")
        auth_token = os.getenv("TWILIO_AUTH_TOKEN")
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=f"{STOCK_NAME}: 🔺{percentage}%\nHeadline: {news['title']}\nBrief: {news['description']}",
            from_=os.getenv("TWILIO_PHONE_NUMBER"),
            to=os.getenv("MY_PHONE_NUMBER")
        )
        print(message.status)

# Optional : Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file 
by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the
 coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file
 by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the
  coronavirus market crash.
"""
