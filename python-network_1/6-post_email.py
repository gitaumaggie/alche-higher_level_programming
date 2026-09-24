#!/usr/bin/python3
"""Sends an email to a URL and displays the response body."""
import sys
import requests


if __name__ == "__main__":
    email = sys.argv[2]
    response = requests.post(sys.argv[1], data={"email": email})
    print(response.text)
