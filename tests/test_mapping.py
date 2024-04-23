# tests/test_mapping.py

import unittest
from mapping import create_map, Map

class TestMapping(unittest.TestCase):
    def test_create_map(self):
        # Test create_map function
        # Example test case:
        # Given a set of sensor readings, the function should return a Map object
        sensor_readings = [
            [1.0, 2.0, 3.0],
            [4.0, 5.0, 6.0],
            [7.0, 8.0, 9.0]
        ]
        expected_map = Map(data=[
            [None, None, None, None, None, None],
            [None, None, None, None, None, None],
            [None, None, (1, 2, 3), None, None, None],
            [None, None, None, None, None, None],
            [None, None, None, None, (4, 5, 6), None],
            [None, None, None, None, None, None],
            [None, None, None, None, None, (7, 8, 9)],
            [None, None, None, None, None, None]
        ])
        created_map = create_map(sensor_readings)
        self.assertEqual(created_map, expected_map)

    def test_map_class(self):
        # Test Map class
        # Example test cases:
        # 1. Test the initialization of the Map class
        data = [
            [None, None, None, None, None, None],
            [None, None, None, None, None, None],
            [None, None, (1, 2, 3), None, None, None],
            [None, None, None, None, None, None],
            [None, None, None, None, (4, 5, 6), None],
            [None, None, None, None, None, None],
            [None, None, None, None, None, (7, 8, 9)],
            [None, None, None, None, None, None]
]
        map_ = Map(data=data)
        self.assertEqual(map_.data, data)

        # 2. Test the equality of two Map objects
        map1 = Map(data=data)
        map2 = Map(data=data)
        self.assertEqual(map1, map2)

        # 3. Test the inequality of two Map objects
        map1 = Map(data=data)
        map2 = Map(data=[
            [None, None, None, None, None, None],
            [None, None, None, None, None, None],
            [None, None, (1, 2, 3), None, None, None],
            [None, None, None, None, (4, 5, 6), None],
            [None, None, None, None, None, None],
            [None, None, None, None, None, (7, 8, 9)],
            [None, None, None, None, None, None],
            [None, None, None, None, None, None]
        ])
        self.assertNotEqual(map1, map2)

if __name__ == '__main__':
    unittest.main()
