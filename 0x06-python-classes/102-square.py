#!/usr/bin/python3
"""definig the Square class."""


class Square:
    """Defining the square class."""

    def __init__(self, size=0):
        """INIT obj.

        Args:
            size: square side len.
        """
        self.size = size

    @property
    def size(self):
        """square side prop.

        Raises:
            TypeError: if size is not int.
            ValueError: If size < 0.
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """the square area function.

        Returns:
            will ret square size.
        """
        return self.__size ** 2

    def __eq__(self, other):
        return self.area() == other.area()

    def __ne__(self, other):
        return self.area() != other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __ge__(self, other):
        return self.area() >= other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __le__(self, other):
        return self.area() <= other.area()
