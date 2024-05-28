#!/usr/bin/python3
"""class to json """

import json


def class_to_json(obj):
    """class to json"""
    return obj.__dict__
