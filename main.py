from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from telegram import Telegram
from email_manager import send_emails

FLIGHT_FROM = 'LIS'

sheety = DataManager()
sheet_data = sheety.get_data()
users_list = sheety.get_users_list()

def format_telegram_message(flight_data):
    price = flight_data.price
    departure_city_name = flight_data.departure_city_name
    departure_airport_iata_code = flight_data.departure_airport_iata_code
    arrival_city_name = flight_data.arrival_city_name
    arrival_airport_iata_code = flight_data.arrival_airport_iata_code
    outbound_date = flight_data.outbound_date
    inbound_date = flight_data.inbound_date
    url = flight_data.url
    message = f"Low price alert! Only {price}EUR to fly from {departure_city_name}-{departure_airport_iata_code} to {arrival_city_name}-{arrival_airport_iata_code}, from {outbound_date} to {inbound_date}"
    if flight_data.stopovers > 0:
        message += f'\n\nFlight has 1 stop over, via {flight_data.via_city}'
    message += f'\n{url}'
    return message

for city in sheet_data:
    if city['iataCode'] == '':
        data_manager = FlightSearch()
        iata_code = data_manager.get_iata_code(city['city'])
        sheety.put_iata_code(id=city['id'], iata_code=iata_code)
    else:
        iata_code = city['iataCode']
    flight_data = FlightData()
    # flight_data.get_flights(FLIGHT_FROM, iata_code)
    # print(flight_data)
    if flight_data.get_flights(FLIGHT_FROM, iata_code) and flight_data.price <= city['lowestPrice']:
        message = format_telegram_message(flight_data)
        print(message)
        # telegram = Telegram()
        # telegram.send_message(message)
        send_emails(users_list, message)
