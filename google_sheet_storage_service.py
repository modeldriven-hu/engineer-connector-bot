from storage_service import StorageService
from typing import List

import pygsheets

class GoogleSheetStorageService(StorageService):

    def __init__(self) -> None:
        pass
    
    def insert_record(self, values: List) -> None:
        raise NotImplementedError

    def remove_record(self, row: int) -> None:
        raise NotImplementedError

    def list_records(self) -> List:
        raise NotImplementedError