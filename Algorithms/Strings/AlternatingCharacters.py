#!/bin/python3
import sys


def alternatingCharacters(s):
    return sum(s[i] == s[i+1] for i in range(len(s) - 1))


q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    result = alternatingCharacters(s)
    print(result)
