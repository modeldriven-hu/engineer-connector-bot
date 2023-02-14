from abc import abstractmethod
from typing import Protocol

class LocationService(Protocol):

    @abstractmethod
    def store(self, username: str, city: str, country: str):
        raise NotImplementedError

    @abstractmethod
    def remove(self, username: str):
        raise NotImplementedError

    @abstractmethod
    def list_by_name(self, username: str): 
        raise NotImplementedError

    @abstractmethod
    def list_by_location(self, city: str, country: str):
        raise NotImplementedError

    @abstractmethod
    def list_by_proximity(self, city: str, country: str, distance_in_km: int):
        raise NotImplementedError

    @abstractmethod
    def get_map_link(self):
        raise NotImplementedError