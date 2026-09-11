#!/usr/bin/python3
"""
Module defining the Rectangle class that inherits from BaseGeometry.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class representing a rectangle, inheriting from BaseGeometry."""

    def __init__(self, width, height):
        """
        Initialize a new Rectangle.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        # Validate dimensions using the parent's integer_validator
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        # Assign as private attributes
        self.__width = width
        self.__height = height
