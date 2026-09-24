#!/usr/bin/python3
"""Sends a request to a URL and handles HTTP error codes."""
import sys
import requests


if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    if response.status_code >= 400:
        print("Error code:", response.status_code)
    else:
        print(response.text)
