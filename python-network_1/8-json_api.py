#!/usr/bin/python3
"""Sends a POST request with a letter and displays JSON response."""

import sys
import requests


if __name__ == "__main__":
    q = sys.argv[1] if len(sys.argv) > 1 else ""

    data = {"q": q}
    response = requests.post("http://0.0.0.0:5000/search_user", data=data)

    try:
        json_data = response.json()

        if json_data:
            print("[{}] {}".format(json_data.get("id"), json_data.get("name")))
        else:
            print("No result")

    except ValueError:
        print("Not a valid JSON")
