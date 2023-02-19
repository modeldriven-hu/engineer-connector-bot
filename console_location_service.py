from location_service import LocationService, Location
from typing import List, Dict, Set

class ConsoleLocationService(LocationService):

    def __init__(self) -> None:
        self.locations: Dict[str, List[Location]] = {}

    def store(self, username: str, location: Location) -> None:
        if username not in self.locations:
            self.locations[username] = []

        self.locations[username].append(location)

    def remove(self, username: str) -> None:
        try:
            self.locations.pop(username)
        except KeyError:
            pass

    def list_by_name(self, username: str) -> List[Location]:
        return self.locations.get(username,[])
        
    def list_by_location(self, location: Location) -> Set[str]:
        result = set()
        for key, values in self.locations.items():
            for value in values:
                if value == location:
                    result.add(key)

        return result

    def get_map_link(self) -> str:
        return 'http://fake.com/map'
