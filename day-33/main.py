from datetime import datetime
import smtplib
import requests

MY_LONGITUDE = 19.040236
MY_LATITUDE = 47.497913
USERNAME = "USERNAME"
PASSWORD = "PASSWORD"
sunrise = ""
sunset = ""
response = ""
data = ""
ISS_long = 0
ISS_lat = 0


def is_iss_overhead():
    global response, data, ISS_long, ISS_lat
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    print(response.status_code)
    data = response.json()
    ISS_long = float(data["iss_position"]["longitude"])
    ISS_lat = float(data["iss_position"]["latitude"])
    print(ISS_long)
    print(ISS_lat)
    if MY_LONGITUDE - 5 <= ISS_long <= MY_LONGITUDE + 5 and MY_LATITUDE - 5 <= ISS_lat <= MY_LATITUDE + 5:
        return True


is_iss_overhead()


def is_night():
    global response, data, sunrise, sunset
    parameters = {
        "lat": MY_LATITUDE,
        "lng": MY_LONGITUDE,
        "formatted": 0
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = data["results"]["sunrise"]
    sunset = data["results"]["sunset"]
    print(data)
    print(sunrise.split("T")[1].split(":")[0])
    print(sunset.split("T")[1].split(":")[0])

    time_now = datetime.now()
    print(time_now.hour)

    if time_now >= sunset or time_now <= sunrise:
        return True
