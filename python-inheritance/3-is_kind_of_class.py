#!/usr/bin/python3
"""This module provides a function to check if an object is an instance
of, or inherited from, a specified class."""


def is_kind_of_class(obj, a_class):
    """Return True if obj is an instance of a_class or a subclass of it,
    otherwise False."""
    return isinstance(obj, a_class)
