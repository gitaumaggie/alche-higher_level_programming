#!/usr/bin/python3
"""Provides a function for adding two integers or floats."""


def add_integer(a, b=98):
    """Add two integers or floats and return their integer sum."""
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
