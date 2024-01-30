#!/usr/bin/python3
"""this module is for the add integer function."""


def add_integer(a, b=98):
    """this will simply adds two integers

    Args:
        a: 1st int.
        b: 2nd int with defult value (98).

    Raises:
        TypeError: if the variables not int or float.

    Returns:
        will ret the 2 int sum.
    """

    if type(a) not in (int, float):
        raise TypeError('a must be an integer')
    if type(b) not in (int, float):
        raise TypeError('b must be an integer')
    return int(a) + int(b)

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
