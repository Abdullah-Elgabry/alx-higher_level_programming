#!/usr/bin/python3
"""this module represinting py script"""


import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

db = list(sys.argv[1:])

try:
    dfdb = load_from_json_file('add_item.json')
except Exception:
    dfdb = []

dfdb.extend(db)
save_to_json_file(dfdb, 'add_item.json')
