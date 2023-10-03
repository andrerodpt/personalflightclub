import requests
from datetime import datetime
from dateutil.relativedelta import relativedelta
import json
from credentials import TEQUILA_API_KEY

class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self) -> None:
        self.tequila_base_url = 'https://api.tequila.kiwi.com'
        self.tequila_api_headers = {
            'apiKey': TEQUILA_API_KEY,
            'Accept': 'application/json'
        }
        self.price = 0,
        self.departure_city_name = ''
        self.departure_airport_iata_code = ''
        self.arrival_city_name = ''
        self.arrival_airport_iata_code = ''
        self.outbound_date = ''
        self.inbound_date = ''
        self.url = ''
        self.stopovers = 0
        self.via_city = ''

    def get_flights(self, iata_origin, iata_destination):
        current_date = datetime.now()
        date_to = current_date + relativedelta(months=6)
        search_flights_url = f'{self.tequila_base_url}/search'
        search_flights_params = {
            'fly_from': iata_origin,
            'fly_to': iata_destination,
            'date_from': current_date.strftime('%d/%m/%Y'),
            'date_to': date_to.strftime('%d/%m/%Y'),
            'nights_in_dst_from': 7,
            'nights_in_dst_to': 28,
            'limit': 1,
            'max_stopovers': 2
        }
        try:
            response = requests.get(url=search_flights_url, headers=self.tequila_api_headers, params=search_flights_params)
            response.raise_for_status()
            self.price = json.loads(response.text)['data'][0]['price']
            self.departure_city_name = json.loads(response.text)['data'][0]['cityFrom']
            self.departure_airport_iata_code = json.loads(response.text)['data'][0]['flyFrom']
            self.arrival_city_name = json.loads(response.text)['data'][0]['cityTo']
            self.arrival_airport_iata_code = json.loads(response.text)['data'][0]['flyTo']
            self.outbound_date = datetime.fromtimestamp(json.loads(response.text)['data'][0]['route'][0]['dTime']).strftime('%Y-%m-%d')
            self.inbound_date = datetime.fromtimestamp(json.loads(response.text)['data'][0]['route'][-1]['dTime']).strftime('%Y-%m-%d')
            self.url = json.loads(response.text)['data'][0]['deep_link']
            if len(json.loads(response.text)['data'][0]['route']) > 2:
                self.stopovers = 1
                self.via_city = json.loads(response.text)['data'][0]['route'][0]['cityTo']
            return True
        except IndexError as e: 
            return False