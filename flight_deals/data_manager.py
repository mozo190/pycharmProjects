import os
import requests
from requests.auth import HTTPBasicAuth

class DataManager:
    def __init__(self):
        self._user = os.environ.get("SHEETY_USER")
        self._password = os.environ.get("SHEETY_PASSWORD")
        self.authorization = HTTPBasicAuth(self._user, self._password)
        self.destination_data = {}

    def get_data(self):
        # 2. Use the Sheety API to GET all the data in that sheet and print it out.
        response = requests.get(url=os.environ.get("SHEETY_ENDPOINT"), auth=self.authorization)
        response.raise_for_status()
        self.destination_data = response.json()["prices"]
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
