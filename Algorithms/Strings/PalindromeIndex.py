#!/bin/python3
import sys


def palindromeIndex(s):
    start = 0
    end = len(s) - 1
    while start < end:
        if s[start] != s[end]:
            if s[start+1:start+3] == s[end:end-2:-1]:
                return start
            elif s[start:start+2] == s[end-1:end-3:-1]:
                return end
        start += 1
        end -= 1
    return -1


q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    result = palindromeIndex(s)
    print(result)
