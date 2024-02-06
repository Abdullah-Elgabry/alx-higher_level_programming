#!/usr/bin/python3
"""this module represinting read_file func"""


def read_file(filename=""):
    """this func reads the file"""
    with open(filename, encoding='utf-8') as fl:
        print(fl.read(), end="")
