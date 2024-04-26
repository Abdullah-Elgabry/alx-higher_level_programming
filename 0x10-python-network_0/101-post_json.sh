#!/bin/bash
# this curl script will post a json request and display the request body..

curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
