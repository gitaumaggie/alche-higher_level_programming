#!/usr/bin/python3
"""Defines a function that returns an object's dictionary representation."""


def class_to_json(obj):
    """Return the dictionary description of an object."""
    return obj.__dict__
