#!/usr/bin/python3
"""this module represinting load_from_json_file func"""


import json


def load_from_json_file(filename):
    """this func will reads all obj in json file"""
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
