#!/usr/bin/python3
"""Student class"""


class Student():
    """A student class

    Args:
    first_name: first name of student
    last_name: last name of student
    age: age of student
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary representation of a Student"""
        return self.__dict__
