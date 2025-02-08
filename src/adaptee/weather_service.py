import requests
import json
import yaml
from src.domain.city import City


class WeatherApi:

    def get_current_temperatures(self):
        locations_to_retrieve = self.get_locations()
        weatherapi_api_key = self.get_api_key()
        locations_weather = []

        for location in locations_to_retrieve:
            city_info = self.get_city_info(location['name'], weatherapi_api_key)
            city = City()
            city.set_name(location['name'])
            city.set_longitude(city_info.json()['location']['lon'])
            city.set_latitude(city_info.json()['location']['lat'])
            city.set_current_temperature(city_info.json()['current']['temp_c'])
            locations_weather.append(city.to_dict())

        return yaml.dump(locations_weather, default_flow_style=False)

    def get_api_key(self):
        try:
            with open('../../config/secrets.json') as config_file:
                return json.load(config_file)['weatherapi_api_key']
        except IOError as e:
            print(f"An IOError occurred during reading weatherapi_api_key: {e}")
            raise e

    def get_locations(self):
        try:
            with open('../../config/locations.json', 'r') as location_file:
                return json.load(location_file)['locations']
        except IOError as e:
            print(f"An IOError occurred during reading locations.json: {e}")
            raise e

    def get_city_info(self, city_name, weatherapi_api_key):
        try:
            url = f'http://api.weatherapi.com/v1/current.json?key={weatherapi_api_key}&q={city_name}&aqi=no'
            return requests.get(url)
        except requests.exceptions.RequestException as e:
            print(f"An error occurred during retrieving data from weatherapi: {e}")
            raise e
