#!/usr/bin/python3
"""Defines a JSON file-writing function."""
import json


def save_to_json_file(my_obj, filename):
    """Write an object to a text file using JSON representation."""
    with open(filename, "w") as f:
        json.dump(my_obj, f)


def load_from_json_file(filename):
    """Create an object from a JSON file."""
    with open(filename, "r") as f:
        return json.load(f)
