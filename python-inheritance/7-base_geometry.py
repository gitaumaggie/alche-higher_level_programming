#!/usr/bin/python3
"""Define a geometry class with area and integer validation methods."""


class BaseGeometry:
    """Provide an area interface and validate positive integers."""

    def area(self):
        """Raise an exception because area is not yet implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is a positive integer."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
