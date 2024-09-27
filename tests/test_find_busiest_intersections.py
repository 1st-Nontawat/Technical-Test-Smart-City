import unittest
from find_busiest_intersections import find_busiest_intersections

class TestFindBusiestIntersections(unittest.TestCase):
    def test_single_busiest_intersection(self):
        data = {'A': 10, 'B': 15, 'C': 7}
        self.assertEqual(find_busiest_intersections(data), ['B'])

    def test_multiple_busiest_intersections(self):
        data = {'A': 10, 'B': 15, 'C': 15}
        self.assertEqual(find_busiest_intersections(data), ['B', 'C'])
    
    def test_empty_data(self):
        data = {}
        self.assertEqual(find_busiest_intersections(data), [])
    
    def test_all_same_vehicle_count(self):
        data = {'A': 10, 'B': 10, 'C': 10}
        self.assertEqual(find_busiest_intersections(data), ['A', 'B', 'C'])

    def test_one_intersection(self):
        data = {'A': 10}
        self.assertEqual(find_busiest_intersections(data), ['A'])

if __name__ == '__main__':
    unittest.main()
