import os

import requests

IATA_ENDPOINT = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
FLIGHT_ENDPOINT = "https://test.api.amadeus.com/v2/shopping/flight-offers"
TOKEN_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.api_key = os.environ.get("FLIGHT_API_KEY")
        self.api_secret = os.environ.get("FLIGHT_API_SECRET")
        self._token = self._get_new_token()

    def get_destination_code(self, city_name):
        print(f"Using this token to get destination code: {self._token}")
        headers = {"authorization": f"Bearer {self._token}"}  # "Bearer " + self._token

        query = {
            "keyword": city_name,
            "max": "2",
            "include": "AIRPORTS"
        }

        response = requests.get(url=IATA_ENDPOINT, headers=headers, params=query)
        print(f"Status code: {response.status_code}. Airport IATA: {response.text}")
        try:
            code = response.json()["data"][0]["iataCode"]
        except IndexError:
            print(f"IndexError: No airport found for {city_name}")
            return "N/A"
        except KeyError:
            print(f"KeyError: No airport found for {city_name}")
            return "Not found"
        return code

    # def search(self):
    #     response = requests.get(url=self.endpoint, headers=self.headers, params=self.params)
    #     response.raise_for_status()
    #     data = response.json()
    #     print(data)
    #     return data

    def _get_new_token(self):
        header = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        body = {
            "grant_type": "client_credentials",
            "client_id": self.api_key,
            "client_secret": self.api_secret
        }
        response = requests.post(url=TOKEN_ENDPOINT, headers=header, data=body)
        print(f"Your token is: {response.json()['access_token']}")
        print(f"Your token expires in: {response.json()['expires_in']} seconds")
        return response.json()["access_token"]
