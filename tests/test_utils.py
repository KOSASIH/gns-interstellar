# tests/test_utils.py

import unittest
from utils import Vector3D, is_close

class TestUtils(unittest.TestCase):
    def test_vector3d_class(self):
        # Test Vector3D class
        # Example test cases:
        # 1. Test the initialization of the Vector3D class
        vector = Vector3D(x=1.0, y=2.0, z=3.0)
        self.assertIsInstance(vector, Vector3D)

        # 2. Test the equality of two Vector3D objects
        vector1 = Vector3D(x=1.0, y=2.0, z=3.0)
        vector2 = Vector3D(x=1.0, y=2.0, z=3.0)
        self.assertEqual(vector1, vector2)

        # 3. Test the inequality of two Vector3D objects
        vector1 = Vector3D(x=1.0, y=2.0, z=3.0)
        vector2 = Vector3D(x=4.0, y=5.0, z=6.0)
        self.assertNotEqual(vector1, vector2)

    def test_is_close(self):
        # Test is_close function
        # Example test cases:
        # 1. Test the equality of two floating point numbers within a tolerance
        self.assertTrue(is_close(1.0, 1.0, tolerance=1e-6))
        self.assertTrue(is_close(1.0, 1.000001, tolerance=1e-6))
        self.assertFalse(is_close(1.0, 1.00001, tolerance=1e-6))

if __name__ == '__main__':
    unittest.main()
