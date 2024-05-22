#!/usr/bin/python3
""" Module that contains the BaseGeometry class """


class BaseGeometry:
    """Class representing base geometry."""

    def area(self):
        """Compute the area. This method raises an Exception."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate if value is an integer greater than 0."""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
