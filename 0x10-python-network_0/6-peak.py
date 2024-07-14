#!/usr/bin/python3
"""finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    if (list_of_integers) is None or list_of_integers == []:
        return None

    high = len(list_of_integers) - 1
    low = 0

    while low <= high:
        mid = ((high - low) // 2) + low

        if high == 0:
            return list_of_integers[0]
        if high == 1:
            return max(list_of_integers)
        if list_of_integers[mid] >= list_of_integers[mid - 1] and \
           list_of_integers[mid] >= list_of_integers[mid + 1]:
            return list_of_integers[mid]
        elif mid > 0 and list_of_integers[mid] < list_of_integers[mid + 1]:
            low = mid + 1
        else:
            high = mid - 1
