#!/bin/python3
import sys


# Build a string of length at least n starting with i
def build_str(i, n):
    res = ""
    while len(res) < n:
        res += str(i)
        i += 1
    return res


def solve(s):
    for i in range(1, len(s) // 2 + 1):
        first = int(s[:i])
        if build_str(first, len(s)) == s:
            return "YES " + str(first)
    return "NO"


q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    print(solve(s))
    
