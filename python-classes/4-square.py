#!/usr/bin/python3
"""Defines a Square class with a validated size property."""


class Square:
    """Represents a square with a private, validated size."""

    def __init__(self, size=0):
        """Initialize a Square with the given size."""
        self.size = size

    @property
    def size(self):
        """Return the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size after validating its type and value."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square."""
        return self.__size ** 2
