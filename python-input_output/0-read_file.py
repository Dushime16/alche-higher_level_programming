#!/usr/bin/python3
"""Module that reads a text file and prints it."""


def read_file(filename=""):
    """Read a UTF8 text file and print it to stdout."""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
