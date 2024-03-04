#!/usr/bin/python3
"""Insert line to a file"""


def append_after(filename="", search_string="", new_string=""):
    """function that inserts a line of text to a file,
    after each line containing a specific string"""
    spc_line = []
    with open(filename, 'r', encoding="utf-8") as f:
        for line in f:
            spc_line += [line]
            if line.find(search_string) != -1:
                spc_line += [new_string]

    with open(filename, 'w', encoding="utf-8") as f:
        f.write("".join(spc_line))
