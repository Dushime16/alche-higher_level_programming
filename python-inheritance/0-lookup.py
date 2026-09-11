#!/usr/bin/python3
"""This module provides a function to retrieve all attributes
and methods of an object."""


def lookup(obj):
    """Return a list of available attributes and methods
    of the given object."""
    return dir(obj)
