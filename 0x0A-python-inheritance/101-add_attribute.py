#!/usr/bin/python3
"""adds a new attribute to an object if it’s possible"""


def(obj, attributes, value):
    """add attribute"""
        if '__dict__' not in dir(obj):
            raise TypeError("can't add new attribute")
        if '__slots__' in dir(obj):
            raise TypeError("can't add new attribute")
        else:
            setattr(obj, attribute, value)
