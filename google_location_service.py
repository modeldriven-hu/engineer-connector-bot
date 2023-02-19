from location_service import LocationService, Location
from dotenv import load_dotenv
from os import getenv
from google_sheet_storage_service import GoogleSheetStorageService
from typing import List, Set, Dict

class GoogleLocationService(LocationService):

    def __init__(self) -> None:
        """
        Initialize the GoogleLocationService object and load environment variables.
        """
        super().__init__()
        load_dotenv()
        self.storage = GoogleSheetStorageService(getenv('GOOGLE_SHEET_ID'), getenv('GOOGLE_KEY_FILE'))

    def store(self, username: str, location: Location) -> None:
        """
        Store the location information for a user in the Google Sheet.

        :param username: The username of the user.
        :param city: The city where the user is located.
        :param country: The country where the user is located.
        """        
        self.storage.insert_record([username, location.city, location.country])

    def remove(self, username: str)-> None:
        """
        Remove the location information for a user from the Google Sheet.

        :param username: The username of the user.
        """
        records_to_remove = []

        for index, r in enumerate(self.storage.list_records(), start = 2):
            if r['username'] == username:
                records_to_remove.append(index)        
                
        # delete from the end of the list going backwards
        for index in records_to_remove[::-1]:                
            self.storage.remove_record(index)

    def list_by_name(self, username: str) -> List[Location]:
        """
        Get the location information for a user by their username.

        :param username: The username of the user.
        :return: A list with the city and country where the user is located.
        """        

        locations = []

        for r in self.storage.list_records():
            if r['username'] == username:
                locations.append(Location(r['city'], r['country']))        

        return locations        

    def list_by_location(self, city: str, country: str)-> Set[str]:

        locations = set()

        for r in self.storage.list_records():
            if r['city'].casefold() == city.casefold():
                locations.add(r['username'])

        return locations

    def get_map_link(self) -> str:
        return 'http://fake.com/map'

# service = GoogleLocationService()
# service.store('john.doe', 'Budapest', 'Hungary')
# service.store('jane.doe', 'Budapest', 'Hungary')
# service.store('john.doe', 'Budapest', 'Hungary')
# service.remove('john.doe')