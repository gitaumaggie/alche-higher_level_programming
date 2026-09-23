#!/bin/bash
# Sends an OPTIONS request and displays the HTTP methods accepted by the server.
curl -s -I -X OPTIONS "$1" | grep -i '^Allow:' | cut -d' ' -f2-
