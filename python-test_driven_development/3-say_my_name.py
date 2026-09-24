#!/usr/bin/python3
"""Provide a function for printing a person's full name.

The function validates that both names are strings before
displaying them in the required format.
"""


def say_my_name(first_name, last_name=""):
    """Print the supplied first and last names.

    Args:
        first_name: The person's first name as a string.
        last_name: The person's last name, defaulting to an empty string.

    Raises:
        TypeError: If either argument is not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
