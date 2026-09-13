#!/usr/bin/python3
"""Defines a custom list class."""


class MyList(list):
    """A list subclass with a method to print a sorted copy."""

    def print_sorted(self):
        """Print the list sorted in ascending order."""
        print(sorted(self))
