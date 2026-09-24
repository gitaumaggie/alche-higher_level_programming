#!/usr/bin/python3
"""Displays the value of the X-Request-Id response header."""
import sys
import requests


if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    print(response.headers.get("X-Request-Id"))
