#!/usr/bin/python3
"""
Defining Rectangle class
"""
class Rectangle:
    """Rrectangle class init"""

    number_of_instances = 0
    """instance num"""

    print_symbol = '#'
    """this # will print to get the shape"""

    def __init__(self, width=0, height=0):
        """this is the Constructor.

        Args:
            width: rectangle width.
            height: rectangle height.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """this Prop is shows the rect width.

        Raises:
            TypeError: if width found not int.
            ValueError: if width < 0.
        """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """this Prop is shows the rect height.

        Raises:
            TypeError: if width found not int.
            ValueError: if width < 0.
        """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """function to return the rect area"""
        return self.width * self.height

    def perimeter(self):
        """function to return the rect area"""
        if not self.width or not self.height:
            return 0
        return (self.width + self.height) * 2

    def __str__(self):
        """this func will print rect str"""
        if not self.width or not self.height:
            return ""
        return ((str(self.print_symbol) * self.width + "\n") *
                self.height)[:-1]

    def __repr__(self):
        """func aims to reproduction"""
        return "Rectangle(" + str(self.width) + ", " + str(self.height) + ")"

    def __del__(self):
        """this func will popup msg when del a Rectangle."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
