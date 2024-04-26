#!/bin/bash
# this will send and display the request.
curl -s "$1" | wc -c
