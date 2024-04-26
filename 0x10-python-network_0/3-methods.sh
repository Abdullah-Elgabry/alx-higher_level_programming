#!/bin/bash
# this curl script will show the * accepted HTTP methods.
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
