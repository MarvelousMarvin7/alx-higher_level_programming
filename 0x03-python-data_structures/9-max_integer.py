#!/usr/bin/python3
"""return maximum integer"""


def max_integer(my_list=[]):
    length = range(len(my_list))
    if len(my_list) == 0:
        return 'None'
    max_num = my_list[0]
    for i in length:
        if my_list[i] > max_num:
            max_num = my_list[i]
    return max_num
