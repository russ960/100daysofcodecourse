import creds
import requests
from flight_data import FlightData

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.base_url = "https://tequila-api.kiwi.com"
        self.header = {
            "apikey": creds.flight_key
        }

    def get_iata_code(self, city_name):
        url = self.base_url + "/locations/query"
        payload = {
            "term": city_name,
            "locale": "en-US",
            "location_types": "airport",
            "limit": 10,
            "active_only": "true"
        }
        response = requests.get(url=url, params=payload, headers=self.header)
        return response.json()["locations"][0]["code"]

    def search_flight_cost(self, depart_iata, destination_iata, start_date, stop_date):
        url = self.base_url + "/v2/search"
        payload = {
            "fly_from": depart_iata,
            "fly_to": destination_iata,
            "date_from": start_date,
            "date_to": stop_date,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "adults": 1,
            "curr": "GBP"
        }
        try:
            response = requests.get(url=url, params=payload, headers=self.header).json()['data'][0]
        except IndexError:
            print(f"No flights for {destination_iata}")
            return None
        flight = FlightData(destination_iata, response["cityTo"], response["flyFrom"], response["cityFrom"], response["local_departure"].split("T")[0], response["local_arrival"].split("T")[0], response["price"])
        return flight
