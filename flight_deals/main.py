
import time
from datetime import datetime, timedelta

from notification_manager import NotificationManager
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import find_cheapest_flight

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

sheet_data = data_manager.get_data()
print(sheet_data)

ORIGIN_CITY_IATA = "LON"

#=========update iata codes===================#
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
    print(f"Getting flights for {destination}")
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    cheapest_flight = find_cheapest_flight(flight)
    # print(f"{destination['city']}: {cheapest_flight.price} HUF")
    # time.sleep(2)

#=======send message=================#

    if cheapest_flight.price != "N/A" and cheapest_flight.price < destination["lowestPrice"]:
        print(f"Lower price flight found to {destination['city']}!")
        # notification_manager.send_sms(
        #     message=f"Low price alert! Only {cheapest_flight.price} HUF to fly from {cheapest_flight.origin_airport}"
        #             f" to {cheapest_flight.destination_airport}, from {cheapest_flight.out_date}"
        #             f" to {cheapest_flight.return_date}"
        # )
        notification_manager.send_whatsapp(
            message_body=f"Low price alert! Only {cheapest_flight.price} HUF to fly "
                         f" from {cheapest_flight.origin_airport},"
                         f" on {cheapest_flight.out_date} until {cheapest_flight.return_date}."
        )
