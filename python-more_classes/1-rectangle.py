#!/usr/bin/python3
"""Defines a Rectangle class with validated dimensions."""


class Rectangle:
    """Represent a rectangle with width and height."""

    def __init__(self, width=0, height=0):
        """Initialize a rectangle with validated dimensions."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Return the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set and validate the width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Return the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set and validate the height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
