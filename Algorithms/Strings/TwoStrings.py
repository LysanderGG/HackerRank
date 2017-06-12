#!/bin/python3
import sys


# Just return if there is a common letter
def twoStrings(s1, s2):
    return len(set(s1) & set(s2)) > 0


q = int(input().strip())
for a0 in range(q):
    s1 = input().strip()
    s2 = input().strip()
    result = twoStrings(s1, s2)
    print("YES" if result else "NO")
