from location_service import LocationService
from typing import List, Set, Dict

class ConsoleLocationService(LocationService):

    def __init__(self) -> None:
        self.locations: Dict[str, List[Dict[str, str]]] = {}

    def store(self, username: str, city: str, country: str) -> None:
        if username not in self.locations:
            self.locations[username] = []

        self.locations[username].append({'city': city, 'country': country})

    def remove(self, username: str) -> None:
        try:
            self.locations.pop(username)
        except KeyError:
            pass

    def list_by_name(self, username: str) -> List[Dict[str, str]]:
        return self.locations.get(username,[])
        
    def list_by_location(self, city: str, country: str) -> Set[str]:
        result = set()
        for key, values in self.locations.items():
            for location in values:
                if location['city'] == city and location['country'] == country:
                    result.add(key)

        return result

    def list_by_proximity(self, city: str, country: str, distance_in_km: int) -> Set[str]:
        return self.list_by_location(city, country)

    def get_map_link(self) -> str:
        return 'http://fake.com/map'
