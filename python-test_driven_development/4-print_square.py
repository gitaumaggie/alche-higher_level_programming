#!/usr/bin/python3
"""Provide a function that prints a square using the # character.

The square's width and height are determined by a non-negative
integer supplied by the caller.
"""


def print_square(size):
    """Print a square of the specified size using # characters.

    Args:
        size: A non-negative integer specifying the square's dimensions.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is a negative integer.
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
