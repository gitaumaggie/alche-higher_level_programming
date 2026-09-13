#!/usr/bin/python3
"""Module containing a function to inspect an object"""


def lookup(obj):
    """Return the list of available attributes and methods of an object"""
    return dir(obj)
