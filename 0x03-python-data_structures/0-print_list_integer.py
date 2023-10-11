#!/usr/bin/python3
# print all integers of a list
def print_list_integer(my_list=[]):
    length = range(len(my_list))
    for i in length:
        print("{:d}".format(my_list[i]))
