#!/usr/bin/python3
"""Script that adds all arguments
to a Python list, and then save them to a file	"""

import sys
import os.path

filename = "add_item.json"
""" Check if the file exists, if it does,
load the content of the file into my_list, if not, create an empty list"""


def json(my_list, f):
    pass


if os.path.exists(filename):
    with open(filename, 'r') as f:
        my_list = json.load(f)
else:
    my_list = []

for i in range(1, len(sys.argv)):
    my_list.append(sys.argv[i])

with open(filename, 'w') as f:
    json.dump(my_list, f)
