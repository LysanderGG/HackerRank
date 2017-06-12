#!/bin/python3
import sys


def pangrams(s):
    return "pangram" if len(set(s.replace(' ','').lower())) == 26 else "not pangram"


s = input().strip()
result = pangrams(s)
print(result)
