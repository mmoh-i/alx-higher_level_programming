#!/usr/bin/python3
# A script that sends a request to the URL
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    res = requests.get(url)
    if r.status_code >= 400:
        print("Error code: {}".format(res.status_code))
    else:
        print(res.text)
