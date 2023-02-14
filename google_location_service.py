from location_service import LocationService
import pygsheets

class GoogleLocationService(LocationService):

    def __init__(self) -> None:
        super().__init__()

    def store(self, username: str, city: str, country: str):
        raise NotImplementedError

    def remove(self, username: str):
        raise NotImplementedError

    def list_by_name(self, username: str): 
        raise NotImplementedError

    def list_by_location(self, city: str, country: str):
        raise NotImplementedError

    def list_by_proximity(self, city: str, country: str, distance_in_km: int):
        raise NotImplementedError

    def get_map_link(self):
        raise NotImplementedError