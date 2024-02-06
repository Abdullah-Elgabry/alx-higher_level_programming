#!/usr/bin/python3
"""this module represinting append_after func"""


def append_after(filename="", search_string="", new_string=""):
    """ this def will add line but  with condition"""

    with open(filename, 'r', encoding='utf-8') as f:
        line_list = []
        while True:
            line = f.readline()
            if line == "":
                break
            line_list.append(line)
            if search_string in line:
                line_list.append(new_string)
    with open(filename, 'w', encoding='utf-8') as f:
        f.writelines(line_list)
