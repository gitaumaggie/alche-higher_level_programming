#!/usr/bin/python3
"""Defines a function that writes text to a UTF-8 file."""


def write_file(filename="", text=""):
    """Write text to a file and return the number of characters written."""
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
