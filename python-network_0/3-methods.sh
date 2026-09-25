#!/bin/bash
# Displays all HTTP methods the server will accept for the URL passed as argument
curl -sI "$1" | grep -i "^Allow:" | cut -d ' ' -f2-
