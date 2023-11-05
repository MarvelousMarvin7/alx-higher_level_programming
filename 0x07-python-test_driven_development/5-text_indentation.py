#!/usr/bin/python3
"""Text indentation"""


def text_indentation(text):
    """
    a function that prints a text with 2 new lines after each of these
    characters: ., ? and :

    Args:
    text : text to be printed

    Return:
    Nothing

    Raise:
    TypeError : text must be a string
    If text is not string
    """
    if not isinstance(text, str):
        raise TypeError('text must be a string')

    l = " "
    string = ""

    if text is "":
        print(string, end='')

    for s in text:
        if s is l and s is ' ':
            l = s
            continue
        if (l is '.' or l is '?' or l is ':') and s is ' ':
            l = s
            continue
        if s is '.' or s is '?' or s is ':':
            string += s + '\n' + '\n'
            l = s
        else:
            string += s
            l = s
    print(string.rstrip(' '), end='')
