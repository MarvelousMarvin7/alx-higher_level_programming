#!/usr/bin/python3
"""Inherits from Int"""


class MyInt(int):
    """class"""
    def __eq__(self, other):
        return int(str(self)) != other

    def __ne__(self, other):
        return int(str(self)) == other
