#!/bin/python3
import sys
import collections


def sherlockAndAnagrams(s):
    nb_pairs = 0
    d = {}
    for sub_size in range(1, len(s)):
        for i in range(len(s) - sub_size + 1):
            sub = "".join(sorted(s[i:i+sub_size]))
            d[sub] = d.get(sub, 0) + 1
    return sum((v - 1) * v // 2 for v in d.values()) # = n choose 2 for each value.


q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    result = sherlockAndAnagrams(s)
    print(result)
