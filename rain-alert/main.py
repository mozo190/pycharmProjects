import requests

# API_KEY: "cb39ed815882577596774c580048f8a3"

parameters = {
    "lat": 44.34,
    "lon": 10.99,
    "appid": "cb39ed815882577596774c580048f8a3",
    "cnt": 4
}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast?", params=parameters)
response.raise_for_status()
weather_data = response.json()
#print status code
print(response.status_code)
print(weather_data)

#print "Bring an Umbrella" if any of the weather condition codes is less than 700 in the next 12 hours
weather_slice = weather_data["list"][:12]
for hour_data in weather_slice:
    weather_code = hour_data["weather"][0]["id"]
    if int(weather_code) < 700:
        print("Bring an umbrella")
        break
    else:
        print("No need for an umbrella")
        break
