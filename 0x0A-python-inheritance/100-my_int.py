#!/usr/bin/python3
"""
this is for test the inherit
"""


class MyInt(int):
    """myint class will have 3 core functions to inherit """
    def __new__(cls, *args, **kwargs):
        """this func will make an instance from the class"""
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, other):
        """checks equalization"""
        return int(self) != other

    def __ne__(self, other):
        """rev the eq func"""
        return int(self) == other
