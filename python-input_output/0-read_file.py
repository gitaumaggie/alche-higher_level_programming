#!/usr/bin/python3
"""Defines a function that reads and prints a UTF-8 text file."""


def read_file(filename=""):
    """Read a UTF-8 text file and print its contents."""
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
