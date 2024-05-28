#!/usr/bin/python3
""" la madre del que se copie """


class student:
    """ la madre del que se copie"""

    def __init__(self, first_name, last_name, age):
        """ la madre del que se copie"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

        def to_json(self):
            """ la madre del que se copie"""
            return self.__dict__
