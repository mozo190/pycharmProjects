import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response.status_code)

data = response.json()
long = float(data["iss_position"]["longitude"])
lat = float(data["iss_position"]["latitude"])
print(long)
print(lat)
