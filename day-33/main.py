from datetime import datetime
import smtplib
import requests

MY_LONGITUDE = 19.040236
MY_LATITUDE = 47.497913
USERNAME = "USERNAME"
PASSWORD = "PASSWORD"

response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response.status_code)

data = response.json()
long = float(data["iss_position"]["longitude"])
lat = float(data["iss_position"]["latitude"])
print(long)
print(lat)

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

if MY_LONGITUDE - 5 <= long <= MY_LONGITUDE + 5 and MY_LATITUDE - 5 <= lat <= MY_LATITUDE + 5:
    if time_now.hour >= int(sunset.split("T")[1].split(":")[0]) or time_now.hour <= int(sunrise.split("T")[1].split(":")[0]):
        print("Look up")
        try:
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user="USERNAME", password="PASSWORD")
                connection.sendmail(from_addr="USERNAME", to_addrs="USERNAME",
                                    msg="Subject:Look up\n\nThe ISS is above you in the sky.")
        except smtplib.SMTPAuthenticationError:
            print("Failed to authenticate.")
