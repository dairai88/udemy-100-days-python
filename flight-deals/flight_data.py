"""flight data"""
import json

class FlightData:
    # pylint: disable=missing-class-docstring
    def __init__(self, price, origin_airport, dest_airport, out_date, return_date, stops):
        self.price = price
        self.origin_airport = origin_airport
        self.dest_airport = dest_airport
        self.out_date = out_date
        self.return_date = return_date
        self.stops = stops


def find_cheapest_flight(flight_data):
    """find cheapest flight"""
    if flight_data is None or not flight_data['data']:
        print("No flight data")
        return FlightData("N/A", "N/A", "N/A", "N/A", "N/A", "N/A")

    first_flight = flight_data['data'][0]
    flight_stops = len(first_flight["itineraries"][0]["segments"]) - 1
    lowest_price = float(first_flight["price"]["grandTotal"])
    origin = first_flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
    destination = first_flight["itineraries"][0]["segments"][flight_stops]["arrival"]["iataCode"]
    out_date = first_flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
    # pylint: disable=line-too-long
    return_date = first_flight["itineraries"][1]["segments"][flight_stops]["departure"]["at"].split("T")[0]

    cheapest_flight = FlightData(lowest_price, origin, destination, out_date, return_date, flight_stops)

    for flight in flight_data["data"]:
        price = float(flight["price"]["grandTotal"])

        if price < lowest_price:
            flight_stops = len(flight["itineraries"][0]["segments"]) - 1
            lowest_price = price
            origin = flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
            destination = flight["itineraries"][0]["segments"][flight_stops]["arrival"]["iataCode"]
            out_date = flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
            # pylint: disable=line-too-long
            return_date = flight["itineraries"][1]["segments"][flight_stops]["departure"]["at"].split("T")[0]
            cheapest_flight = FlightData(lowest_price, origin, destination, out_date, return_date, flight_stops)

    return cheapest_flight


if __name__ == '__main__':
    with open("sample_response2.json", encoding="utf-8") as file:
        data = json.load(file)
        _cheapest_flight = find_cheapest_flight(data)
        print(f"Lowest price to {_cheapest_flight.dest_airport} is ¥{_cheapest_flight.price}")
