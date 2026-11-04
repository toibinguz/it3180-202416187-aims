import unittest
from aims.dvd import DigitalVideoDisc
from aims.search import search_by_title, search_by_category


class TestSearch(unittest.TestCase):

    def setUp(self):
        self.dvd1 = DigitalVideoDisc("The Lion King", "Animation", "Roger Allers", 87, 19.95)
        self.dvd2 = DigitalVideoDisc("Star Wars", "Science Fiction", "George Lucas", 87, 24.95)
        self.dvd3 = DigitalVideoDisc("Aladdin", "Animation", cost=18.99)
        self.items = [self.dvd1, self.dvd2, self.dvd3]

    def test_search_by_category(self):
        results = search_by_category(self.items, "animation")
        self.assertEqual(len(results), 2)
        self.assertIn(self.dvd1, results)
        self.assertIn(self.dvd3, results)

    def test_search_by_title_case_insensitive(self):
        results = search_by_title(self.items, "lion")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].title, "The Lion King")


if __name__ == "__main__":
    unittest.main()
