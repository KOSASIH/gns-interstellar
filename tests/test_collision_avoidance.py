# tests/test_collision_avoidance.py

import unittest
from collision_avoidance import avoid_collision, CollisionAvoidance

class TestCollisionAvoidance(unittest.TestCase):
    def test_avoid_collision(self):
        # Test avoid_collision function
        # Example test case:
        # Given a current position and a target position, the function should return a new position that avoids collision
        current_position = (1.0, 2.0, 3.0)
        target_position = (4.0, 5.0, 6.0)
        obstacles = [(2.0, 3.0, 4.0), (3.0, 4.0, 5.0)]
        avoidance = CollisionAvoidance()
        new_position = avoidance.avoid_collision(current_position, target_position, obstacles)
        self.assertNotEqual(new_position, target_position)
        self.assertTrue(avoidance.is_safe(new_position, obstacles))

    def test_collision_avoidance_class(self):
        # Test CollisionAvoidance class
        # Example test cases:
        # 1. Test the initialization of the CollisionAvoidance class
        avoidance = CollisionAvoidance()
        self.assertIsInstance(avoidance, CollisionAvoidance)

        # 2. Test the is_safe method
        avoidance = CollisionAvoidance()
        position = (1.0, 2.0, 3.0)
        obstacles = [(2.0, 3.0, 4.0), (3.0, 4.0, 5.0)]
        self.assertFalse(avoidance.is_safe(position, obstacles))

if __name__ == '__main__':
    unittest.main()
