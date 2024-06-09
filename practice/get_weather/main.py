import requests
from twilio.rest import Client
import os

WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"
WEATHER_URL_FORECAST = "https://api.openweathermap.org/data/2.5/forecast"
weather_api_key = os.environ.get("WEATHER_API_KEY")
twilio_sid = os.environ.get("TWILIO_SID")
twilio_auth = os.environ.get("TWILIO_AUTH")
twilio_phone_from = os.environ.get("TWILIO_PHONE")
twilio_phone_to = os.environ.get("TWILIO_PHONE_2")

TARGET = input("Enter city name: ")

# response = requests.get(url=f"{WEATHER_URL}?q={TARGET}&appid={WEATHER_API_KEY}")
# response.raise_for_status()
# weather_data = response.json()
# print(f"{TARGET} coordinates are as follows: \n{weather_data['coord']}")

params = {
    # "lon": weather_data['coord']['lon'],
    # "lat": weather_data['coord']['lat'],
    "lon": 19.0399,
    "lat": 47.498,
    "appid": weather_api_key,
    "cnt": 3,
}
# response_forecast = requests.get(url=f"{WEATHER_URL_FORECAST}?lat={lat_}&lon={lon_}&appid={WEATHER_API_KEY}")
response_forecast = requests.get(WEATHER_URL_FORECAST, params=params)
response_forecast.raise_for_status()

weather_data_forecast = response_forecast.json()
# forecast_weather_id_ = weather_data_forecast['list'][0]['weather'][0]['id']
# print(forecast_weather_id_)

# for i in range(3):
#     var = weather_data_forecast['list'][i]['weather'][0]['id']
#     if var < 700:
#         print("Bring an umbrella")

list_ = weather_data_forecast['list']

rain = False


def rain_message():
    print(f"In {var_time} Bring an umbrella")


for i in list_:
    var = i['weather'][0]['id']
    if var < 700:
        var_time = i['dt_txt']
        rain_message()
        client = Client(twilio_sid, twilio_auth)

        message = client.messages.create(
            body=f"In {var_time} Bring an umbrella",
            from_=twilio_phone_from,
            to=twilio_phone_to
        )
        print(message.sid)
