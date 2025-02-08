import http.server
import json
import socketserver
import folium

from src.adapter.adapter import JSONAdapter


class Server:
    PORT = 8181

    def __init__(self):
        self.adapter = None

    def set_adapter(self, adapter: JSONAdapter):
        self.adapter = adapter

    def show_temperatures(self):
        all_location = self.adapter.get_temperatures_json()
        self.create_map(all_location)
        self.start_server()

    def create_map(self, all_locations):
        map_serbia = folium.Map(location=[44.0, 20.0], zoom_start=7)
        all_locations = json.loads(all_locations["locations"])
        for location in all_locations:
            name = location['name']
            coordination = [location['latitude'], location['longitude']]
            temperature = location['current_temperature']
            folium.Marker(
                location=coordination,
                popup=f'{temperature}. {name}',
                icon=folium.DivIcon(html=f'''
                    <div style="width: 30px; height: 30px; background-color: lightblue; 
                            color: black; font-size: 16px; font-weight: bold; 
                            text-align: center; line-height: 30px; 
                            border-radius: 5px;">
                {temperature}
                </div>
                ''')
            ).add_to(map_serbia)

        map_serbia.save("index.html")

    def start_server(self):
        handler = http.server.SimpleHTTPRequestHandler

        with socketserver.TCPServer(("", self.PORT), handler) as httpd:
            httpd.serve_forever()
