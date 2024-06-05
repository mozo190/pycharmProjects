import os

import requests
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

forecast_url = os.getenv('FORECAST_URL')
api_key = os.getenv('API_KEY')

account_sid = os.getenv('ACCOUNT_SID')
auth_token = os.getenv('AUTH_TOKEN')

parameters = {
    "lat": 44.34,
    "lon": 10.99,
    "appid": api_key,
    "cnt": 4
}

response = requests.get(forecast_url, params=parameters)
response.raise_for_status()
weather_data = response.json()
# print status code
print(response.status_code)
print(weather_data)

# print "Bring an Umbrella" if any of the weather condition codes is less than 700 in the next 12 hours
weather_slice = weather_data["list"][:12]
for hour_data in weather_slice:
    weather_code = hour_data["weather"][0]["id"]
    if int(weather_code) < 700:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body="Bring an umbrella",
            from_=os.getenv('FROM_PHONE_NUMBER'),
            to=os.getenv('TO_PHONE_NUMBER')
        )
        print(message.status)
    else:
        print("No need for an umbrella")
        break
