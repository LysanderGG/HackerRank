#!/bin/python3
import sys


def funnyString(s):    
    return all(abs(ord(s[i]) - ord(s[i+1])) == abs(ord(s[-i-1]) - ord(s[-i-2])) for i in range(len(s) - 1))


q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    result = funnyString(s)
    print("Funny" if result else "Not Funny")
