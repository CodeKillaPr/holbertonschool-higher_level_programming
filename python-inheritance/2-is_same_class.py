#!/usr/bin/python3
""" module that contains a class """


def is_same_class(obj, a_class):
    """ Check if obj is exactly an instance of a_class. """

    if type(obj) == a_class:
        return True

    else:
        return False
