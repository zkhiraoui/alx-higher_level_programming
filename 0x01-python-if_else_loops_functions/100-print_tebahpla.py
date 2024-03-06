#!/usr/bin/python3

""""Print the alphabet in reverse order alternating upper- and lower-case."""
for i in range(122, 96, -1):
    print("{}".format(chr(i) if i % 2 == 0 else chr(i - 32)), end='')
