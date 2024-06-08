import os
import requests

from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData

data_manager = DataManager()
flight_search = FlightSearch()

sheet_data = data_manager.get_data()
print(sheet_data)

if sheet_data[0]["iataCode"] == "":
    for city in sheet_data:
        city["iataCode"] = flight_search.get_destination_code(city["city"])
        data_manager.destination_data = sheet_data
        data_manager.update_data(sheet_data.index(city), city)
        data_manager.save_data()
        print(city)
else:
    print("IATA Codes already exist in the data.")
    print(sheet_data)
    print("No changes made.")

