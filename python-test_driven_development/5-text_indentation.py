#!/usr/bin/python3
"""Provide a function that formats text after specific punctuation.

The function prints two newline characters after periods,
question marks and colons while removing surrounding whitespace.
"""


def text_indentation(text):
    """Print formatted text with two newlines after . ? and :.

    Args:
        text: The string to format and print.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    line = ""

    for char in text:
        if char in ".?:":
            line = line.strip() + char
            print(line, end="\n\n")
            line = ""
        else:
            line += char

    if line.strip():
        print(line.strip(), end="")
