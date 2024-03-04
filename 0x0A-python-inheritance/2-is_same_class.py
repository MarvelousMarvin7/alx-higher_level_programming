#!/usr/bin/python3
"""class of an object verification"""


def is_same_class(obj, a_class):
    """Check if an oject is of an exact class

    Args:
    obj: object to be checked
    a_class: class to verify

    Return: True else false
    """
    if type(obj) is a_class:
        return True
    return False
