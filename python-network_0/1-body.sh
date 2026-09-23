#!/bin/bash
# Sends a GET request and displays the response body only for a 200 status code.
curl -s -o /tmp/body -w '%{http_code}' "$1" | grep -q '^200$' && cat /tmp/body
