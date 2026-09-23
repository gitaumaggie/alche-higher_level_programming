#!/bin/bash
# Sends a GET request with the required user ID header and displays the response body.
curl -s -H "X-HolbertonSchool-User-Id: 98" "$1"
