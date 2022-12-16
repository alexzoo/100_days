from dotenv import load_dotenv
import os
import requests

load_dotenv()
SHEETY_FLIGHT_AUTH = os.getenv('SHEETY_FLIGHT_AUTH')
sheety_endpoint = 'https://api.sheety.co/7fc06cccc3669df91d5a3cc4ff4cc754/flightDeals/prices'
sheety_headers = {
    'Authorization': SHEETY_FLIGHT_AUTH
}


class DataManager:

    # This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):

        resp = requests.get(url=sheety_endpoint, headers=sheety_headers)
        resp.raise_for_status()
        self.destination_data = resp.json()['prices']
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                'price': {
                    'iataCode': city['iataCode']
                }
            }
            resp = requests.put(url=f'{sheety_endpoint}/{city["id"]}', json=new_data, headers=sheety_headers)
            print(resp.text)
