# tests/test_positioning.py

import unittest
from positioning import calculate_position, Position

class TestPositioning(unittest.TestCase):
    def test_calculate_position(self):
        # Test calculate_position function
        # Example test case:
        # Given a set of sensor readings, the function should return the correct position
        sensor_readings = [1.0, 2.0, 3.0]
        expected_position = Position(x=1.0, y=2.0, z=3.0)
        calculated_position = calculate_position(sensor_readings)
        self.assertEqual(calculated_position, expected_position)

    def test_position_class(self):
        # Test Position class
        # Example test cases:
        # 1. Test the initialization of the Position class
        position = Position(x=1.0, y=2.0, z=3.0)
        self.assertEqual(position.x, 1.0)
        self.assertEqual(position.y, 2.0)
        self.assertEqual(position.z, 3.0)

        # 2. Test the equality of two Position objects
        position1 = Position(x=1.0, y=2.0, z=3.0)
        position2 = Position(x=1.0, y=2.0, z=3.0)
        self.assertEqual(position1, position2)

        # 3. Test the inequality of two Position objects
        position1 = Position(x=1.0, y=2.0, z=3.0)
        position2 = Position(x=4.0, y=5.0, z=6.0)
        self.assertNotEqual(position1, position2)

if __name__ == '__main__':
    unittest.main()
