#!/bin/bash
# this curl script will sends request and prith the request stat..

curl -s -o /dev/null -w "%{http_code}" "$1"
