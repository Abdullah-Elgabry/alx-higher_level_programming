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

    @property
    def size(self):
        """Getter or setter the square size."""
        return self.__size
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """get square function.

        Returns:
            The size square size.
        """
        return self.__size ** 2
