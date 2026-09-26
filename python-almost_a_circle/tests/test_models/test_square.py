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

    def tearDown(self):
        try:
            os.remove("Square.json")
        except IOError:
            pass

    def test_square_1_arg(self):
        s = Square(1)
        self.assertEqual(s.size, 1)

    def test_square_2_args(self):
        s = Square(1, 2)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.x, 2)

    def test_square_3_args(self):
        s = Square(1, 2, 3)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)

    def test_square_4_args(self):
        s = Square(1, 2, 3, 4)
        self.assertEqual(s.id, 4)

    def test_size_type_error(self):
        with self.assertRaises(TypeError):
            Square("1")

    def test_x_type_error(self):
        with self.assertRaises(TypeError):
            Square(1, "2")

    def test_y_type_error(self):
        with self.assertRaises(TypeError):
            Square(1, 2, "3")

    def test_size_value_error(self):
        with self.assertRaises(ValueError):
            Square(-1)
        with self.assertRaises(ValueError):
            Square(0)

    def test_x_value_error(self):
        with self.assertRaises(ValueError):
            Square(1, -2)

    def test_y_value_error(self):
        with self.assertRaises(ValueError):
            Square(1, 2, -3)

    def test_str(self):
        s = Square(5, 2, 1, 12)
        self.assertEqual(str(s), "[Square] (12) 2/1 - 5")

    def test_to_dictionary(self):
        s = Square(10, 2, 1, 1)
        self.assertEqual(s.to_dictionary(), {'id': 1, 'size': 10, 'x': 2, 'y': 1})

    def test_update_args(self):
        s = Square(5)
        s.update(89)
        self.assertEqual(s.id, 89)
        s.update(89, 1)
        self.assertEqual(s.size, 1)
        s.update(89, 1, 2)
        self.assertEqual(s.x, 2)
        s.update(89, 1, 2, 3)
        self.assertEqual(s.y, 3)

    def test_update_kwargs(self):
        s = Square(5)
        s.update(**{'id': 89})
        self.assertEqual(s.id, 89)
        s.update(**{'id': 89, 'size': 1})
        self.assertEqual(s.size, 1)
        s.update(**{'id': 89, 'size': 1, 'x': 2})
        self.assertEqual(s.x, 2)
        s.update(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual(s.y, 3)

    def test_create(self):
        s1 = Square.create(**{'id': 89})
        self.assertEqual(s1.id, 89)
        s2 = Square.create(**{'id': 89, 'size': 1})
        self.assertEqual(s2.size, 1)
        s3 = Square.create(**{'id': 89, 'size': 1, 'x': 2})
        self.assertEqual(s3.x, 2)
        s4 = Square.create(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual(s4.y, 3)

    def test_save_to_file_none(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_empty(self):
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_squares(self):
        s = Square(1, 0, 0, 1)
        Square.save_to_file([s])
        with open("Square.json", "r") as f:
            self.assertIn('"id": 1', f.read())

    def test_load_from_file_not_exist(self):
        if os.path.exists("Square.json"):
            os.remove("Square.json")
        self.assertEqual(Square.load_from_file(), [])

    def test_load_from_file_exists(self):
        s = Square(1)
        Square.save_to_file([s])
        self.assertEqual(len(Square.load_from_file()), 1)


if __name__ == "__main__":
    unittest.main()
