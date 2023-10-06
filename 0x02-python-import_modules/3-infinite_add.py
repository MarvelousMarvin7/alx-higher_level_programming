#!/usr/bin/python3
"""Addition of argument"""


if __name__ == "__main__":
    import sys

    """access the lenght of arguments to be added
    if there is no argument print 0
    else sum all argument using sum function
    """
    add = len(sys.argv) - 1
    if add == 0:
        print("0")
    else:
        total = sum(int(sys.argv[i + 1]) for i in range(add))
        print("{}".format(total))
