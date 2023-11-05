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

    last = " "
    string = ""

    if text is "":
        print(string, end='')

    for s in text:
        if s is last and s is ' ':
            last = s
            continue
        if (last is '.' or last is '?' or last is ':') and s is ' ':
            last = s
            continue
        if s is '.' or s is '?' or s is ':':
            string += s + '\n' + '\n'
            last = s
        else:
            string += s
            last = s
    print(string.rstrip(' '), end='')
