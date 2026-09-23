#!/bin/bash
# Sends a GET request and displays the response body only for a 200 status code.
curl -s -w '%{http_code}' -o /tmp/body "$1" | grep -q 200 && cat /tmp/body
