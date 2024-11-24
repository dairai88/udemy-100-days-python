"""flight search"""
import os
from datetime import datetime
import requests

BASE_URL = "https://api.amadeus.com"

class FlightSearch:
    """flight search"""

    def __init__(self) -> None:
        self._api_key = os.environ["AMADEUS_API_KEY"]
        self._api_secret = os.environ["AMADEUS_API_SECRET"]
        self._token = self._get_new_token()
        self.headers= { "Authorization": f"Bearer {self._token}" }

    def search_iata_code(self, city):
        """search iata code"""
        city_endpoint = f"{BASE_URL}/v1/reference-data/locations/cities"
        params = { "keyword": city, "include": "AIRPORTS", "max": 3 }

        response = requests.get(url=city_endpoint, params=params, headers=self.headers, timeout=20)
        response.raise_for_status()

        try:
            code = response.json()["data"][0]['iataCode']
        except IndexError:
            print(f"IndexError: No airport code found for {city}.")
            return "N/A"
        except KeyError:
            print(f"KeyError: No airport code found for {city}.")
            return "Not Found"

        return code

    def _get_new_token(self):
        """get new token"""
        token_endpoint = f"{BASE_URL}/v1/security/oauth2/token"

        header = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        body = {
            'grant_type': 'client_credentials',
            'client_id': self._api_key,
            'client_secret': self._api_secret
        }

        response = requests.post(url=token_endpoint, headers=header, data=body, timeout=20)
        return response.json()["access_token"]

    def search_flight(self,
                      origin_city_code,
                      dest_city_code,
                      from_time: datetime,
                      to_time: datetime,
                      is_direct):
        """search flight"""
        search_endpoint = f"{BASE_URL}/v2/shopping/flight-offers"

        if is_direct:
            nonStop = "true"
        else:
            nonStop = "false"

        params = {
            "originLocationCode": origin_city_code,
            "destinationLocationCode": dest_city_code,
            "departureDate": from_time.strftime("%Y-%m-%d"),
            "returnDate": to_time.strftime("%Y-%m-%d"),
            "adults": 1,
            "nonStop": nonStop,
            "currencyCode": "CNY",
            "max": 10
        }

        response = requests.get(
            url=search_endpoint,
            headers=self.headers,
            params=params,
            timeout=20
        )
        response.raise_for_status()

        if response.status_code != 200:
            print(f"search_flight() response code: {response.status_code}")
            print("There was a problem with the flight search.\n"
                  "For details on status codes, check the API documentation: \n"
                  "https://developers.amadeus.com/self-service/category/flights/"
                  "api-doc/flight-offers-search/api-reference")
            print("Response body:", response.text)
            return None

        return response.json()
