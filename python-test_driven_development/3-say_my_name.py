#!/usr/bin/python3
"""Module to print a name
"""


def say_my_name(first_name, last_name=""):
    """Function to print a name
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
