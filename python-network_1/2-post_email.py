#!/usr/bin/python3
"""Sends an email to a URL and displays the decoded response body."""
import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    email = sys.argv[2]
    data = urllib.parse.urlencode({"email": email}).encode("utf-8")
    with urllib.request.urlopen(sys.argv[1], data=data) as response:
        print(response.read().decode("utf-8"))
