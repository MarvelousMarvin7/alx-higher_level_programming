#!/usr/bin/python3
"""Inheritance from list"""


class MyList(list):
    """Inherit from list class"""

    def print_sorted(self):
        """print sorted list"""
        print(sorted(self))
