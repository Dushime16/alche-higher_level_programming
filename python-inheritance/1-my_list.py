#!/usr/bin/python3
"""This module defines a class MyList that inherits from list."""


class MyList(list):
    """A class that inherits from list and adds a sorted print method."""

    def print_sorted(self):
        """Print the list in ascending sorted order without modifying it."""
        print(sorted(self))
