import os
from pprint import pprint

import requests
from requests.auth import HTTPBasicAuth


class DataManager:
    def __init__(self):
        self._user = os.environ.get("SHEETY_USER")
        self._password = os.environ.get("SHEETY_PASSWORD")
        self.authorization = HTTPBasicAuth(self._user, self._password)
        self.destination_data = {}
        print(f"Authorization: {self.authorization}")

    def get_data(self):
        # 2. Use the Sheety API to GET all the data in that sheet and print it out.
        headers = {
            "Authorization": f"Bearer {os.environ.get('SHEET_AUTH_TOKEN')}"
        }

        flight_sheet_url = os.environ.get("SHEETY_ENDPOINT", "Message not found")

        sheety_response = requests.get(url=flight_sheet_url, headers=headers, auth=self.authorization)
        print(f"sheety_response: {sheety_response}")
        print(f"Response text: {sheety_response.text}")
        sheety_response.raise_for_status()
        data = sheety_response.json()
        self.destination_data = sheety_response.json()["prices"]
        pprint(data)
        return self.destination_data

    def update_destination_codes(self):
        # 4. Update the IATA Codes in the Sheety data.
        for city in self.destination_data:
            sheety_params = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            sheety_response = requests.put(
                url=f"{os.environ.get('SHEETY_ENDPOINT')}/{city['id']}",
                json=sheety_params,
                headers={
                    "Authorization": f"Bearer {os.environ.get('SHEET_AUTH_TOKEN')}"
                },
                auth=self.authorization
            )
            print(sheety_response.text)
