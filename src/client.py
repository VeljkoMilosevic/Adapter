from adapter import JSONAdapter
from server import Server
from weather_api import WeatherApi

weather_api = WeatherApi()
json_adapter = JSONAdapter()
json_adapter.set_weather_api(weather_api)
server = Server()
server.set_adapter(json_adapter)
server.show_temperature()

