import requests

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# print(response.status_code)
#
# data = response.json()
# long = float(data["iss_position"]["longitude"])
# lat = float(data["iss_position"]["latitude"])
# print(long)
# print(lat)

parameters = {
    "lat": 47.497913,
    "lng": 19.040236
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
print(data)
