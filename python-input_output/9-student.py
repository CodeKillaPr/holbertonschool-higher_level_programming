#!/usr/bin/python3
""" la madre del que se copie """


class Student:
    """ la madre del que se copie"""

    def __init__(self, first_name, last_name, age):
        """ la madre del que se copie"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

        def to_json(self):
            """ la madre del que se copie"""
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age
        }
