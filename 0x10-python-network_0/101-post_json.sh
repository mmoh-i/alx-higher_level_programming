#!/bin/bash
# seds a JSON request to URL passed as the first argument, and display the body of the response
curl -s -X POST "$1" -H "Content-Type: application/json" -d @"$2"
