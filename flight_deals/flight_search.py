import os


class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
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