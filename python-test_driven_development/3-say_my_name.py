#!/usr/bin/python3
"""
This is the "3-say_my_name" module.
"""


def say_my_name(first_name, last_name=""):
	"""

	Args:
		first_name (_type_): _description_
		last_name (str, optional): _description_. Defaults to "".

	Raises:
		TypeError: _description_
		TypeError: _description_
	"""
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
