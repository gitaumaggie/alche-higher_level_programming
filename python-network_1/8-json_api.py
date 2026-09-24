#!/usr/bin/python3
"""Sends a POST request and displays a user from the JSON response."""
import sys
import requests


if __name__ == "__main__":
    q = ""
    if len(sys.argv) > 1:
        q = sys.argv[1]

    response = requests.post(
        "http://0.0.0.0:5000/search_user",
        data={"q": q}
    )

    try:
        result = response.json()
        if result:
            print("[{}] {}".format(result.get("id"), result.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
