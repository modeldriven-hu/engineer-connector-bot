import unittest
from google_location_service import GoogleLocationService

class TestGoogleLocationService(unittest.TestCase):
    def setUp(self):
        self.service = GoogleLocationService()

    def test_store(self):
        self.service.store('johndoe', 'New York', 'USA')
        locations = self.service.list_by_name('johndoe')
        self.assertIn({'city':'New York', 'country':'USA'}, locations)

    def test_remove(self):
        self.service.store('janedoe', 'San Francisco', 'USA')
        self.service.remove('janedoe')
        locations = self.service.list_by_name('janedoe')
        self.assertEqual(locations, [])

    def test_list_by_name(self):
        self.service.store('johndoe', 'New York', 'USA')
        self.service.store('johndoe', 'London', 'UK')
        locations = self.service.list_by_name('johndoe')
        self.assertIn({'city':'New York', 'country':'USA'}, locations)
        self.assertIn({'city':'London', 'country':'UK'}, locations)

    def test_list_by_location(self):
        self.service.store('johndoe', 'New York', 'USA')
        self.service.store('janedoe', 'New York', 'USA')
        locations = self.service.list_by_location('New York', 'USA')
        self.assertIn('johndoe', locations)
        self.assertIn('janedoe', locations)

    def test_get_map_link(self):
        link = self.service.get_map_link()
        self.assertEqual(link, 'http://fake.com/map')

if __name__ == '__main__':
    unittest.main()