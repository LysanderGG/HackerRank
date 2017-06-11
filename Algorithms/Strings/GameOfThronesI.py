#!/bin/python3
import sys
import collections


# Check that there is at most 1 letter repeated an odd number of times
def gameOfThrones(s):
    return sum(val % 2 != 0 for val in collections.Counter(s).values()) <= 1
    

s = input().strip()
result = "YES" if gameOfThrones(s) else "NO"
print(result)
