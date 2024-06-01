import requests

MY_LONGITUDE = 19.040236

MY_LATITUDE = 47.497913

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# print(response.status_code)
#
# data = response.json()
# long = float(data["iss_position"]["longitude"])
# lat = float(data["iss_position"]["latitude"])
# print(long)
# print(lat)

parameters = {
    "lat": MY_LATITUDE,
    "lng": MY_LONGITUDE
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
print(data)
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]
print(sunrise)
print(sunset)

