from location_service import LocationService
from dotenv import load_dotenv
from os import getenv
from google_sheet_storage_service import GoogleSheetStorageService

class GoogleLocationService(LocationService):

    def __init__(self) -> None:
        super().__init__()
        load_dotenv()
        self.storage = GoogleSheetStorageService(getenv('GOOGLE_SHEET_ID'), getenv('GOOGLE_KEY_FILE'))

    def store(self, username: str, city: str, country: str):
        self.storage.insert_record([username, city, country])

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

service = GoogleLocationService()
service.store('john.doe','Budapest','Hungary')