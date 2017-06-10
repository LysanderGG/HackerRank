#!/bin/python3
import sys
import collections


def anagram(s):
    if len(s) % 2 == 1:
        return -1
    c = collections.Counter(s[:len(s) // 2]) - collections.Counter(s[len(s) // 2:])
    return sum(item[1] for item in c.items())
    

q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    result = anagram(s)
    print(result)
