#!/bin/bash
# Bash script that takes in a URL, sends a POST request to the passed url.
curl -sL -X POST -d "email=tesst%40gmail.com&subject=I+will+always+be+here+fo+PLD' "$1"
