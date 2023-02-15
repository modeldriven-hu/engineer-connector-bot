from location_service import LocationService

class ConsoleLocationService(LocationService):

    def __init__(self) -> None:
        super().__init__()
        self.locations = dict()

    def store(self, username: str, city: str, country: str):
        if (username not in self.locations):
            self.locations[username] = []

        self.locations[username].append({'city': city, 'country': country})

    def remove(self, username: str):
        if username in self.locations:
            self.locations.pop(username, 0)

    def list_by_name(self, username: str):
        return self.locations[username] if username in self.locations else set()

    def list_by_location(self, city: str, country: str):
        result = set()
        for key, values in self.locations.items():
            for location in values:
                if location['city'] == city and location['country'] == country:
                    result.add(key)

        return result

    def list_by_proximity(self, city: str, country: str, distance_in_km: int):
        return set()

    def get_map_link(self):
        return 'http://fake.com/map'
