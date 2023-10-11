#!/usr/bin/python3
"""replaces an element in a list at a specific position without modifying the original list"""


def new_in_list(my_list, idx, element):
    length = len(my_list)
    new_list = my_list.copy()
    if idx < 0 or idx > length - 1:
        return my_list
    else:
        new_list[idx] = element
        return new_list
