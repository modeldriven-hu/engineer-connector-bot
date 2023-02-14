from abc import abstractmethod
from typing import Protocol, List

class StorageService(Protocol):

    @abstractmethod
    def insert_record(self, values: List) -> None:
        raise NotImplementedError

    @abstractmethod
    def remove_record(self, row: int) -> None:
        raise NotImplementedError

    @abstractmethod
    def list_records(self) -> List:
        raise NotImplementedError