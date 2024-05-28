#!/usr/bin/python3
"""Module that contains a function that
returns an object (Python data structure)"""


def from_json_string(my_str):
    """Function that returns an object (Python data structure)"""
    import json
    return json.loads(my_str)
