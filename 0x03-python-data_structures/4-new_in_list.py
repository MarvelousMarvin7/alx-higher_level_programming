#!/usr/bin/python3
"""replace an element in a list at a position without modifying list"""


def new_in_list(my_list, idx, element):
    length = len(my_list)
    new_list = my_list.copy()
    if idx < 0 or idx > length - 1:
        return my_list
    else:
        new_list[idx] = element
        return new_list
