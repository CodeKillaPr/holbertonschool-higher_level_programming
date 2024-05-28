#!/usr/bin/python3
""" la madre del que se copie """


class Student:
    """ la madre del que se copie"""

    def __init__(self, first_name, last_name, age):
        """ la madre del que se copie """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ la madre del que se copie """

        if attrs is None:
            return self.__dict__

        new_dict = {}
        for key, value in self.__dict__.items():
            if key in attrs:
                new_dict[key] = value
        return new_dict

    def reload_from_json(self, json):
        """ la madre del que se copie """

        for key, value in json.items():
            setattr(self, key, value)
