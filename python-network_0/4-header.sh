#!/bin/bash
# Sends a GET request to a URL with a custom header X-HolbertonSchool-User-Id: 98
curl -s -H "X-HolbertonSchool-User-Id: 98" "$1"
