#!/usr/bin/python3
"""Unittest module for Rectangle class."""
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test Rectangle class functionality."""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_rectangle_instantiation(self):
        r = Rectangle(10, 2, 1, 9, 1)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 9)
        self.assertEqual(r.id, 1)

    def test_type_errors(self):
        with self.assertRaises(TypeError):
            Rectangle("10", 2)
        with self.assertRaises(TypeError):
            Rectangle(10, "2")
        with self.assertRaises(TypeError):
            Rectangle(10, 2, "1")
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 1, "9")

    def test_value_errors(self):
        with self.assertRaises(ValueError):
            Rectangle(-10, 2)
        with self.assertRaises(ValueError):
            Rectangle(10, -2)
        with self.assertRaises(ValueError):
            Rectangle(0, 2)
        with self.assertRaises(ValueError):
            Rectangle(10, 0)
        with self.assertRaises(ValueError):
            Rectangle(10, 2, -1)
        with self.assertRaises(ValueError):
            Rectangle(10, 2, 1, -9)

    def test_area(self):
        r = Rectangle(3, 2)
        self.assertEqual(r.area(), 6)

    def test_str(self):
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_to_dictionary(self):
        r = Rectangle(10, 2, 1, 9, 1)
        self.assertEqual(r.to_dictionary(), {'id': 1, 'width': 10, 'height': 2, 'x': 1, 'y': 9})

    def test_update_args(self):
        r = Rectangle(10, 10)
        r.update(89, 1, 2, 3, 4)
        self.assertEqual(str(r), "[Rectangle] (89) 3/4 - 1/2")

    def test_update_kwargs(self):
        r = Rectangle(10, 10)
        r.update(id=89, width=1, height=2, x=3, y=4)
        self.assertEqual(str(r), "[Rectangle] (89) 3/4 - 1/2")

    def test_create(self):
        r = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4})
        self.assertEqual(str(r), "[Rectangle] (89) 3/4 - 1/2")

    def test_save_and_load_file(self):
        r = Rectangle(10, 2)
        Rectangle.save_to_file([r])
        loaded = Rectangle.load_from_file()
        self.assertEqual(len(loaded), 1)
        self.assertEqual(loaded[0].width, 10)


if __name__ == "__main__":
    unittest.main()
