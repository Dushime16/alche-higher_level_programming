#!/usr/bin/python3
"""
Unittest module for Base class.
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """
    Tests instantiation and functionality of the Base class.
    """

    def test_id_auto_increment(self):
        """Test automatic ID assignment when no ID is passed."""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, b1.id + 1)

    def test_id_custom_value(self):
        """Test passing a custom ID."""
        b = Base(89)
        self.assertEqual(b.id, 89)

    def test_id_after_custom(self):
        """Test auto-increment behavior after setting a custom ID."""
        b1 = Base()
        b2 = Base(12)
        b3 = Base()
        self.assertEqual(b3.id, b1.id + 1)


if __name__ == "__main__":
    unittest.main()
