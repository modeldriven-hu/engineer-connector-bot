import unittest
from google_location_service import GoogleLocationService
from location_service import Location

class TestGoogleLocationService(unittest.TestCase):
    def setUp(self):
        self.service = GoogleLocationService()

    def test_store(self):
        self.service.store('johndoe', Location('New York', 'USA'))
        locations = self.service.list_by_name('johndoe')
        self.assertIn(Location('New York', 'USA'), locations)

    def test_remove(self):
        self.service.store('janedoe', Location('San Francisco', 'USA'))
        self.service.remove('janedoe')
        locations = self.service.list_by_name('janedoe')
        self.assertEqual(locations, [])

    def test_list_by_name(self):
        self.service.store('johndoe', Location('New York', 'USA'))
        self.service.store('johndoe', Location('London', 'UK'))
        locations = self.service.list_by_name('johndoe')
        self.assertIn(Location('New York', 'USA'), locations)
        self.assertIn(Location('London', 'UK'), locations)

    def test_list_by_location(self):
        self.service.store('johndoe', Location('New York', 'USA'))
        self.service.store('janedoe', Location('New York', 'USA'))
        locations = self.service.list_by_location(Location('New York', 'USA'))
        self.assertIn('johndoe', locations)
        self.assertIn('janedoe', locations)

    def test_get_map_link(self):
        link = self.service.get_map_link()
        self.assertEqual(link, 'http://fake.com/map')

if __name__ == '__main__':
    unittest.main()