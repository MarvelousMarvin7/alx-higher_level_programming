#!/usr/bin/python3
for a in range(97, 123):
    a = chr(a)
    if a == 'e' or a == 'q':
        continue
    print("{}".format(a), end="")
