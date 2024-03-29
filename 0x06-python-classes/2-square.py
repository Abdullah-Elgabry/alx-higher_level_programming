#!/usr/bin/python3
"""Defining a Square module"""


class Square:
    """Defining a class Square."""

    def __init__(self, size=0):
        """INIT instance.
        Args:
            size (int): represent the square size.
        Raises:
            TypeError: If the size is not an integer
            ValueError: If size is < 0
        """
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
