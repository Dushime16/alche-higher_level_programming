#!/usr/bin/python3
"""Unittest module for Square class."""
import unittest
import os
from models.base import Base
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test Square class functionality."""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_square_instantiation(self):
        s = Square(5, 1, 2, 10)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 1)
        self.assertEqual(s.y, 2)
        self.assertEqual(s.id, 10)

    def test_size_errors(self):
        with self.assertRaises(TypeError):
            Square("5")
        with self.assertRaises(ValueError):
            Square(-5)
        with self.assertRaises(ValueError):
            Square(0)

    def test_str(self):
        s = Square(5, 1, 2, 10)
        self.assertEqual(str(s), "[Square] (10) 1/2 - 5")

    def test_to_dictionary(self):
        s = Square(5, 1, 2, 10)
        self.assertEqual(s.to_dictionary(), {'id': 10, 'size': 5, 'x': 1, 'y': 2})

    def test_update(self):
        s = Square(5)
        s.update(89, 2, 3, 4)
        self.assertEqual(str(s), "[Square] (89) 3/4 - 2")

    def test_create(self):
        s = Square.create(**{'id': 89, 'size': 2, 'x': 3, 'y': 4})
        self.assertEqual(str(s), "[Square] (89) 3/4 - 2")

    def test_save_and_load_file(self):
        s = Square(5)
        Square.save_to_file([s])
        loaded = Square.load_from_file()
        self.assertEqual(len(loaded), 1)
        self.assertEqual(loaded[0].size, 5)


if __name__ == "__main__":
    unittest.main()
