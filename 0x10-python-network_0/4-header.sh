#!/bin/bash
#script to sent GET reaquest to a given URL with a given a header.
curl -sL -H 'X-School-User-Id: 98' "$1"
