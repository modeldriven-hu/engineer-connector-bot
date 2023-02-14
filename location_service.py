from abc import abstractmethod
from typing import Protocol, List, Set, Dict

class LocationService(Protocol):

    @abstractmethod
    def store(self, username: str, city: str, country: str) -> None:
        raise NotImplementedError

    @abstractmethod
    def remove(self, username: str) -> None:
        raise NotImplementedError

    @abstractmethod
    def list_by_name(self, username: str) -> List[Dict[str, str]]: 
        raise NotImplementedError

    @abstractmethod
    def list_by_location(self, city: str, country: str) -> Set[str]:
        raise NotImplementedError

    @abstractmethod
    def list_by_proximity(self, city: str, country: str, distance_in_km: int) -> Set[str]:
        raise NotImplementedError

    @abstractmethod
    def get_map_link(self) -> str:
        raise NotImplementedError