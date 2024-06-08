import os

from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData

flight_sheet_url = os.environ.get("SHEETY_ENDPOINT", "Message not found")


print(flight_sheet_url)