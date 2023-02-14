import unittest
from storage_service import GoogleSheetStorageService

class TestGoogleSheetStorageService(unittest.TestCase):

    def setUp(self) -> None:
        self.service = GoogleSheetStorageService(spreadsheet_id='your-spreadsheet-id', credentials_file_path='credentials.json')
        
    def test_insert_record(self):
        values = ['John', 'Doe', 'john.doe@example.com']
        self.service.insert_record(values)
        records = self.service.list_records()
        self.assertIn(values, records)

    def test_remove_record(self):
        values = ['John', 'Doe', 'john.doe@example.com']
        self.service.insert_record(values)
        records = self.service.list_records()
        self.assertIn(values, records)
        rows_to_remove = [record for record in records if record == values]
        for row in rows_to_remove:
            self.service.remove_record(row=row['row_number'])
        remaining_records = self.service.list_records()
        self.assertNotIn(values, remaining_records)