#!/usr/bin/python3
"""this module represinting write_file func"""


def write_file(filename="", text=""):
    """this func write to file"""
    with open(filename, "w", encoding='utf-8') as fl:
        return fl.write(text)
