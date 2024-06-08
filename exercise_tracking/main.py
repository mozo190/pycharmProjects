import requests
from datetime import datetime
import os

app_id = os.getenv("APP_ID")
api_key = os.getenv("API_KEY")
auth_token = os.getenv("AUTH_TOKEN")
gender = os.getenv("GENDER")
weight = os.getenv("WEIGHT_KG")
height = os.getenv("HEIGHT_CM")
age = os.getenv("AGE")

NUTRI_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENDPOINT = "https://api.sheety.co/039bda9c2fa0b62234cf5f34368a04c8/myWorkout/munkalap1"

exercise_text = input("Tell me which exercises you did: ")
headers = {
    "x-app-id": "2ccdc115",
    "x-app-key": "7efbc10b7e8c364aa5794061936b7088",

}

exercise_params = {
    "query": exercise_text,
    "gender": gender,
    "weight_kg": weight,
    "height_cm": height,
    "age": age,
}
response = requests.post(url=NUTRI_ENDPOINT, json=exercise_params, headers=headers)
result = response.json()
print(result)

headers = {
    "Authorization": "Basic bW96bzE5MDozUkFuZGk3MzMvLy8="
}
today = datetime.now()
date = today.strftime("%d/%m/%Y")
time = today.strftime("%X")
for exercise in result["exercises"]:
    sheety_params = {
        "munkalap1": {
            "date": date,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }
    sheety_response = requests.post(url=SHEETY_ENDPOINT, json=sheety_params, headers=headers)
    print(sheety_response.text)
