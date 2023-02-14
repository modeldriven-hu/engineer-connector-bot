from storage_service import StorageService
from typing import List

import pygsheets

class GoogleSheetStorageService(StorageService):

    def __init__(self, spreadsheet_id: str, credentials_file_path: str) -> None:        
        self.gc = pygsheets.authorize(service_file=credentials_file_path)
        self.sh = self.gc.open_by_key(spreadsheet_id)
        self.worksheet = self.sh.sheet1

    def insert_record(self, values: List) -> None:
        self.worksheet.append_table(values=values)

    def remove_record(self, row: int) -> None:
        self.worksheet.delete_rows(row)

    def list_records(self) -> List:
        return self.worksheet.get_all_records()
