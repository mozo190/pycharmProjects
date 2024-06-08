import os

import requests


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.endpoint = "https://tequila-api.kiwi.com"
        self.api_key = os.environ.get("FLIGHT_API_KEY")
        self.headers = {
            "apikey": self.api_key
        }
        self.params = {
            "term": "London",
            "location_types": "city",
        }

    def get_destination_code(self, city_name):
        self.params["term"] = city_name
        response = requests.get(url=self.endpoint, headers=self.headers, params=self.params)
        response.raise_for_status()
        data = response.json()
        # code = data["locations"][0]["code"]
        code = "TESTING"
        return code

    def search(self):
        response = requests.get(url=self.endpoint, headers=self.headers, params=self.params)
        response.raise_for_status()
        data = response.json()
        print(data)
        return data
