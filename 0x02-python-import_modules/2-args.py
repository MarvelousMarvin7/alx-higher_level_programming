#!/usr/bin/python3
"""Print number of list of an argument"""


if __name__ == "__main__":
    import sys

    """set a variable that counts the number of argument

    if there is no argument print 0 argument
    else print number of argument and list them according to positions:
    """
    count_arg = len(sys.argv) - 1
    if count_arg == 0:
        print("0 arguments.")
    elif count_arg > 1:
        print("{} arguments:".format(count_arg))
    else:
        print("1 argument:")

    # for the list of argument print them with their positions
    for i in range(count_arg):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
