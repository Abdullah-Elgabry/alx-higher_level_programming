#!/usr/bin/python3
"""this module represinting save_to_json_file func"""


import json


def save_to_json_file(my_obj, filename):
    """this def will writes str in file"""
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
