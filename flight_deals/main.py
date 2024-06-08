import os
import time
from datetime import datetime, timedelta

import requests

from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData, find_cheapest_flight

data_manager = DataManager()
flight_search = FlightSearch()

sheet_data = data_manager.get_data()
print(sheet_data)

ORIGIN_CITY_IATA = "LON"

# if sheet_data[0]["iataCode"] == "":
#     for city in sheet_data:
#         city["iataCode"] = flight_search.get_destination_code(city["city"])
#         data_manager.destination_data = sheet_data
#         data_manager.update_data(sheet_data.index(city), city)
#         data_manager.save_data()
#         print(city)
# else:
#     print("IATA Codes already exist in the data.")
#     print(sheet_data)
#     print("No changes made.")

for row in sheet_data:
    if row["iataCode"] == "":
        row["iataCode"] = flight_search.get_destination_code(row["city"])
        time.sleep(2)
print(f"sheet_data:\n {sheet_data}")

data_manager.destination_data = sheet_data
data_manager.update_destination_codes()

#=========search for flights===================#

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    print(f"Getting flights for {destination['city']}....")
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    cheapest_flight = find_cheapest_flight(flight)
    print(f"{destination['city']}: {cheapest_flight.price} HUF")
    time.sleep(2)
