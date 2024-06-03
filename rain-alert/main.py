import requests
# API_KEY: "cb39ed815882577596774c580048f8a3"

parameters = {
    "lat": 44.34,
    "lon": 10.99,
    "appid": "cb39ed815882577596774c580048f8a3"
}

response = requests.get("https://api.openweathermap.org/data/2.5/weather?", params=parameters)
response.raise_for_status()
weather_data = response.json()
#print status code
print(response.status_code)
print(weather_data)

