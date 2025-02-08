from server import Server
from src.adaptee.weather_service import WeatherApi
from src.adapter.adapter import JSONAdapter

weather_api = WeatherApi()
json_adapter = JSONAdapter()
json_adapter.set_weather_api(weather_api)
server = Server()
server.set_adapter(json_adapter)
server.show_temperatures()
