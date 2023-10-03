import requests
import json
from credentials import TEQUILA_API_KEY

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self) -> None:
        self.tequila_base_url = 'https://api.tequila.kiwi.com'
        self.tequila_api_headers = {
            'apiKey': TEQUILA_API_KEY,
            'Accept': 'application/json'
        }

    def get_iata_code(self, city):
        get_city_iata_code_url = f'{self.tequila_base_url}/locations/query'
        get_city_iata_code_params = {
            'term': city,
            'location_types': 'city',
            'limit': 10,
            'active_only': 'true'
        }
        response = requests.get(url=get_city_iata_code_url, headers=self.tequila_api_headers, params=get_city_iata_code_params)
        response.raise_for_status()
        city_iata_code = json.loads(response.text)['locations'][0]['code']
        return city_iata_code