import os
import requests

from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData

data_manager = DataManager()
flight_search = FlightSearch()

sheet_data = data_manager.get_data()
print(sheet_data)

# for row in data["munkalap1"]:
#     if row["iataCode"] == "":
#         flight_search.params["term"] = row["city"]
#         flight_search.params["location_types"] = "city"
#         flight_search.params["limit"] = 1
#         flight_search.params["active_only"] = "true"
#         flight_search.params["sort"] = "popularity"
#         flight_search.params["locale"] = "en-US"
#         flight_search.params["curr"] = "USD"
#         flight_search.params["apikey"] = os.environ.get("FLIGHT_API_KEY")
#         flight_data = flight_search.search()
#         flight_data = FlightData(flight_data)
#         row["iataCode"] = flight_data.iata_code
#         print(flight_data.iata_code)
