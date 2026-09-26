#!/usr/bin/python3
"""Uses GitHub API to display user id using Basic Authentication."""

import sys
import requests


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    url = "https://api.github.com/user"

    response = requests.get(url, auth=(username, password))

    try:
        print(response.json().get("id"))
    except ValueError:
        print("None")
