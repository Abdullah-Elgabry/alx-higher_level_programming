#!/usr/bin/python3
"""this is for the square func."""


def print_square(size):
    """this func will print the squre with hash sympol.

    Args:
        size: squre size.

    Raises:
        TypeError: will raise error in case if size != int.
        ValueError: will raise error in case if less than zero.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    print((("#" * size + "\n") * size), end="")

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
