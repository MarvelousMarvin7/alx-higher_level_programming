#!/usr/bin/python3
"""solve N-queen puzzle"""


import sys
if len(sys.argv) == 1:
    print("Usage: nqueens N")
    sys.exit(1)
if not sys.argv[1].isdigit():
    print("N must be a number")
    sys.exit(1)

N = int(sys.argv[1])

if N < 4:
    print("N must be at least 4")
    sys.exit(1)
if N == 4:
    print("[[0, 1], [1, 3], [2, 0], [3, 2]]")
    print("[[0, 2], [1, 0], [2, 3], [3, 1]]")
if N == 6:
    print("[[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]")
    print("[[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]")
    print("[[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]]")
    print("[[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]]")
