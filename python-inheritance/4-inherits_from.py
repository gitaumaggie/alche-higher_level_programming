#!/usr/bin/python3
"""Defines a function to check class inheritance."""


def inherits_from(obj, a_class):
    """Return True if obj's class is a subclass of a_class."""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
