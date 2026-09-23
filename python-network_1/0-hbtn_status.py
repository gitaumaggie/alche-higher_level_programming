#!/usr/bin/python3
"""Fetches the status of the ALU Intranet and displays its response body."""
import urllib.request


def fetch_status():
    """Fetches the status page and displays its body information."""
    with urllib.request.urlopen("https://alu-intranet.hbtn.io/status") as response:
        body = response.read()
        print("Body response:")
        print("\t- type:", type(body))
        print("\t- content:", body)
        print("\t- utf8 content:", body.decode("utf-8"))


if __name__ == "__main__":
    fetch_status()
