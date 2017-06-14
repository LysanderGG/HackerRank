#!/bin/python3
import sys


def the_love_letter_mystery(s):
    return sum(abs(ord(s[i]) - ord(s[-i-1])) for i in range(len(s) // 2))

    
q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    result = the_love_letter_mystery(s)
    print(result)
