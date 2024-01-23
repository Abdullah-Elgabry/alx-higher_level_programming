#!/usr/bin/python3
"""Defining a Square module"""


class Square:
    """Defining a class Square."""

    def __init__(self, size=0):
        """INIT instance.
        Args:
            size (int): represent the square size.
        """
        self.__size = size

    @property
    def size(self):
        """the Prop for the square side length.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
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

    def my_print(self):
        """print the squre using the hash symp"""
        for y in range(self.size):
            for z in range(self.size):
                print("#", end="\n" if z is self.size - 1 and y != z else "")
            print("")
