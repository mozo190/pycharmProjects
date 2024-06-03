import requests
from dotenv import load_dotenv
import os

load_dotenv()

forecast_url = os.getenv('FORECAST_URL')
api_key = os.getenv('API_KEY')

# print(f"forecast_url: {forecast_url}")
# print(f"api_key: {api_key}")
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
        print("Bring an umbrella")
        break
    else:
        print("No need for an umbrella")
        break
