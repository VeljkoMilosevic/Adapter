class City:
    def __init__(self):
        self.name = None
        self.current_temperature = None
        self.latitude = None
        self.longitude = None

    def set_name(self, name):
        self.name = name

    def set_current_temperature(self, current_temperature):
        self.current_temperature = current_temperature

    def set_latitude(self, latitude):
        self.latitude = latitude

    def set_longitude(self, longitude):
        self.longitude = longitude

    def to_dict(self):
        return {
            "name": self.name,
            "current_temperature": self.current_temperature,
            "latitude": self.latitude,
            "longitude": self.longitude
         }

