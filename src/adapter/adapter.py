import json
import yaml

from src.adaptee.weather_service import WeatherApi


class JSONAdapter:
    def __init__(self):
        self.weather_api = None

    def set_weather_api(self, weather_api: WeatherApi):
        self.weather_api = weather_api

    def get_temperatures_json(self):
        current_temperatures = self.weather_api.get_current_temperatures()
        json_data = json.dumps(yaml.safe_load(current_temperatures), indent=4)
        result = {
            "locations": json_data
        }
        return result
