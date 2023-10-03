import requests
import json
from credentials import SHEETY_BEARER_TOKEN, SHEETY_USERNAME

class DataManager:
    def __init__(self) -> None:
        self.base_url = 'https://api.sheety.co/'
        self.sheety_api_headers = {
            "Authorization": SHEETY_BEARER_TOKEN
        }

    def get_data(self):
        endpoint_url = f'{SHEETY_USERNAME}/flightDeals/prices'
        url = self.base_url + endpoint_url
        response = requests.get(url=url, headers=self.sheety_api_headers)
        response.raise_for_status()
        prices = json.loads(response.text)['prices']
        return prices
    
    def put_iata_code(self, id, iata_code):
        endpoint_url = f'{SHEETY_USERNAME}/flightDeals/prices/{id}'
        url = self.base_url + endpoint_url
        body = {
            "price": {
                "iataCode": iata_code
            }
        }
        response = requests.put(url=url, json=body, headers=self.sheety_api_headers)
        response.raise_for_status()
        return response.text
    
    def get_users_list(self):
        endpoint_url = f"/{SHEETY_USERNAME}/flightDeals/users"
        url = self.base_url + endpoint_url
        headers = {
            "Authorization": SHEETY_BEARER_TOKEN,
            "Content-Type": "application/json",
        }

        response = requests.get(url=url, headers=headers)
        response.raise_for_status()
        return json.loads(response.text)