#!/usr/bin/python3
"""Is instance of class"""


def is_kind_of_class(obj, a_class):
    """Is object an instance of a class

    Args:
    Obj: Object to check
    a_class: Class to verify

    Return: True else False
    """
    if isinstance(obj, a_class):
        return True
    return False
