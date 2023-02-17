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

        list = []

        for index, r in enumerate(self.storage.list_records(), start = 2):
            if r['username'] == username:
                list.append(index)        
                
        # delete from the end of the list going backwards
        for index in list[::-1]:                
            self.storage.remove_record(index)

    def list_by_name(self, username: str): 
        for r in self.storage.list_records():
            if r['username'] == username:
                return {'city':r['city'], 'country': r['country']}            

    def list_by_location(self, city: str, country: str):
        raise NotImplementedError

    def list_by_proximity(self, city: str, country: str, distance_in_km: int):
        raise NotImplementedError

    def get_map_link(self):
        raise NotImplementedError

service = GoogleLocationService()
service.store('john.doe', 'Budapest', 'Hungary')
service.store('jane.doe', 'Budapest', 'Hungary')
service.store('john.doe', 'Budapest', 'Hungary')
service.remove('john.doe')