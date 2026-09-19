#!/usr/bin/python3
"""This module provides a function that writes text to a UTF-8 file."""


def append_write(filename="", text=""):
    """Append a string to a file and return the no of characters written."""
    with open(filename, "a", encoding="utf-8") as f:
        f.write(text)
    return len(text)
