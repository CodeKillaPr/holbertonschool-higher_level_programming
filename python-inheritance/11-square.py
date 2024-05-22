#!/usr/bin/python3
"""Module for Square class."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class that defines a square."""

    def __init__(self, size):
        """Initialize Square instance."""
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """Returns the string representation of Square."""
        return "[Square] {}/{}".format(self.__size, self.__size)
