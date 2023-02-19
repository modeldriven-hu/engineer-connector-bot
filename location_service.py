from abc import abstractmethod
from dataclasses import dataclass
from typing import Protocol, List, Set, Dict

@dataclass
class Location:
    city: str
    country: str

class LocationService(Protocol):

    @abstractmethod
    def store(self, username: str, location: Location) -> None:
        raise NotImplementedError

    @abstractmethod
    def remove(self, username: str) -> None:
        raise NotImplementedError

    @abstractmethod
    def list_by_name(self, username: str) -> List[Location]: 
        raise NotImplementedError

    @abstractmethod
    def list_by_location(self, location: Location) -> Set[str]:
        raise NotImplementedError

    @abstractmethod
    def get_map_link(self) -> str:
        raise NotImplementedError