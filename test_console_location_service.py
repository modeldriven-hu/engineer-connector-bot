import unittest
from console_location_service import ConsoleLocationService

class TestConsoleLocationService(unittest.TestCase):
    def setUp(self):
        self.service = ConsoleLocationService()

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

    def test_list_by_proximity(self):
        self.service.store('johndoe', 'New York', 'USA')
        self.service.store('janedoe', 'London', 'UK')
        self.service.store('bobsmith', 'Sydney', 'Australia')
        locations = self.service.list_by_proximity('New York', 'USA', 10000)
        self.assertIn('johndoe', locations)
        self.assertNotIn('janedoe', locations)
        self.assertNotIn('bobsmith', locations)

    def test_get_map_link(self):
        link = self.service.get_map_link()
        self.assertEqual(link, 'http://fake.com/map')

if __name__ == '__main__':
    unittest.main()