#!/usr/bin/python3
"""Send a POST request with an email parameter and display the response."""

import sys
import urllib.request
import urllib.parse


if __name__ == "__main__":
    data = urllib.parse.urlencode({'email': sys.argv[2]}).encode('ascii')

    with urllib.request.urlopen(sys.argv[1], data) as response:
        print(response.read().decode('utf-8'))
