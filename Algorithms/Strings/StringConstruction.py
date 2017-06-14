#!/bin/python3
import sys


# Same as counting the number of different letters used in s.
def stringConstruction(s):
    return len(set(s))


q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    result = stringConstruction(s)
    print(result)
