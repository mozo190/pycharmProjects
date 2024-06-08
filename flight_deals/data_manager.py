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

    def add_data(self, new_data):
        self.data.append(new_data)

    def update_data(self, index, new_data):
        self.data[index] = new_data

    def delete_data(self, index):
        self.data.pop(index)

    def save_data(self):
        with open("data.txt", mode="w") as file:
            for item in self.data:
                file.write(f"{item}\n")

    def load_data(self):
        with open("data.txt", mode="r") as file:
            self.data = [item.strip() for item in file.readlines()]

    def clear_data(self):
        self.data = []
        self.save_data()

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return str(self.data)
