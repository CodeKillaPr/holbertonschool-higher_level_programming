#!/usr/bin/python3
"""Defines a text-indentation function"""


def max_integer(list=[]):
    """Find the biggest integer of a list."""
    if len(list) == 0:
        return None
    max = list[0]
    for i in list:
        if i > max:
            max = i
    return max
