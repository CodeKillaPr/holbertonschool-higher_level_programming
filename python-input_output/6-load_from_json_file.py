#!/usr/bin/python3
"""Load object from a file"""

import json


def load_from_json_file(filename):
    """Load object from a file"""
    with open(filename, mode='r', encoding='utf-8') as file:
        return json.load(file)
