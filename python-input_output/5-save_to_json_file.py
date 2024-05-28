#!/usr/bin/python3
"""Save object to a file"""
import json


def save_to_json_file(my_obj, filename):
    """ Save object to a file"""
    with open(filename, mode='w', encoding='utf-8') as file:
        json.dump(my_obj, file)
