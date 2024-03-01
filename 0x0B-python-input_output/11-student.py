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

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student"""
        if (type(attrs) == list and all(type(ele) == str for ele in attrs)):
            return {a: getattr(self, a) for a in attrs if hasattr(self, a)}
        return self.__dict__

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance:"""
        for key, value in json.items():
            setattr(self, key, value)
