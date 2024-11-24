"""flight search"""
import time
from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import find_cheapest_flight
from notification_manager import NotificationManager
import dotenv

dotenv.load_dotenv()

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

# Origin airport
ORIGIN_CITY_IATA = "SHA"
customers = data_manager.get_customer_users()

sheet_data = data_manager.sheet_data
for data in sheet_data:
    if data["iataCode"] == "":
        # pylint: disable=invalid-name
        iata_code = flight_search.search_iata_code(data["city"])
        data["iataCode"] = iata_code
        data_manager.update_iata_code(data)

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=6*30)

for destination in sheet_data:
    print(f"\n\nGetting flights for {destination['city']}...")
    flights = flight_search.search_flight(
        origin_city_code=ORIGIN_CITY_IATA,
        dest_city_code=destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today,
        is_direct=True
    )
    if flights is None or not flights['data']:
        flights = flight_search.search_flight(
            origin_city_code=ORIGIN_CITY_IATA,
            dest_city_code=destination["iataCode"],
            from_time=tomorrow,
            to_time=six_month_from_today,
            is_direct=False
        )

    cheapest_flight = find_cheapest_flight(flights)
    print(f"{destination['city']}: ¥{cheapest_flight.price}, ",
          f"expected price: {destination['lowestPrice']}")

    if not cheapest_flight.price == 'N/A' and cheapest_flight.price < destination['lowestPrice']:
        if cheapest_flight.stops == 0:
            content = f"Low price alert! Only {cheapest_flight.price} yen to "\
                  f"fly direct from {ORIGIN_CITY_IATA} to {destination["iataCode"]}, "\
                  f"on {cheapest_flight.out_date} to {cheapest_flight.return_date} \n"\
                  "Get the chance!"
        else:
            # pylint: disable=line-too-long
            content = f"Low price alert! Only {cheapest_flight.price} yen to "\
                  f"fly with {cheapest_flight.stops} stop(s) from {ORIGIN_CITY_IATA} to {destination["iataCode"]}, "\
                  f"on {cheapest_flight.out_date} to {cheapest_flight.return_date} \n"\
                  "Get the chance!"
        notification_manager.send_mail_notification(emails=customers, content=content)

    # Slowing down requests to avoid rate limit
    time.sleep(5)
