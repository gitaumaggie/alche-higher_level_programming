#!/usr/bin/python3
"""Defines a function to check an object's class."""


def is_kind_of_class(obj, a_class):
    """Return True if obj is an instance of a_class or its subclass."""
    return isinstance(obj, a_class)
