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
        return (self.__width * self.__height)

    def perimeter(self):
        """function to return the rect area"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """this func will get the Bigger rect.

        Args:
            rect_1: 1st rect.
            rect_2: 2nd rect.
        Raises:
            TypeError: in these case 1 - 1st rect or 2nd rect is not xxx rect.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)

    @classmethod
    def square(cls, size=0):
        """this func will get inst rect and it's w,h = it's size.

        Args:
            size: rect w,h.
        """
        return (cls(size, size))

    def __str__(self):
        """this func will print rect str"""
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            [rect.append(str(self.print_symbol)) for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """func aims to reproduction"""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)

    def __del__(self):
        """this func will popup msg when del a Rectangle."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
