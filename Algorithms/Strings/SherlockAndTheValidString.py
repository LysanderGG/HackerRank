#!/bin/python3
import sys
import collections


def isValid(s):
    mc = collections.Counter(s).most_common()
    all_equals = all(mc[0][1] == x[1] for x in mc)
    # if only 1 char -> true
    # if all equals but one element that is 1 more than the others
    # if all equals but one element that is 1.
    one_off = len(mc) < 2 or (mc[0][1] - 1 == mc[1][1] and all(mc[1][1] == x[1] for x in mc[1:])) \
                or (mc[-1][1] == 1 and all(mc[0][1] == x[1] for x in mc[:-1]))
    return all_equals or one_off

s = input().strip()
result = isValid(s)
print("YES" if result else "NO")
