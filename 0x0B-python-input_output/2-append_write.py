#!/usr/bin/python3
"""this module represinting append_write func"""


def append_write(filename="", text=""):
    """this func append to file"""
    with open(filename, 'a', encoding="utf-8") as fl:
        return fl.write(text)
