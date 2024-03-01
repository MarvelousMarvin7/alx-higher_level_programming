#!/usr/bin/python3
"""Pascal Triangle Module"""


def pascal_triangle(n):
    """Pascal triangle"""

    if n <= 0:
        return []

    pastri = [[1]]
    while len(pastri) != n:
        tri = pastri[-1]
        temp = [1]
        for i in range(len(tri) - 1):
            temp.append(tri[i] + tri[i + 1])
        temp.append(1)
        pastri.append(temp)
    return pastri
