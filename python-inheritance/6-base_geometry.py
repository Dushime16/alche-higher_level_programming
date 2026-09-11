#!/usr/bin/python3
"""This module defines a class BaseGeometry with an area method."""


class BaseGeometry:
    """A class that serves as a base for geometry classes."""

    def area(self):
        """Raise an Exception indicating area() is not implemented."""
        raise Exception("area() is not implemented")
