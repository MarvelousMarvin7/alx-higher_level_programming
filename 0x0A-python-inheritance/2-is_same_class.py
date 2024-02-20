#!/usr/bin/python3
"""Is same class"""


def is_same_class(obj, a_class):
    """Check if an oject is of a class

    Args:
    obj: object to be checked
    a_class: class to verify

    Return: True else false
    """
    if type(obj) == a_class:
        return True
    return False
