#!/bin/python3
import sys
import collections


def are_happy(ladybug_str):
    if len(ladybug_str) < 2:
        return False
    if ladybug_str[0] != ladybug_str[1]:
        return False
    if ladybug_str[-1] != ladybug_str[-2]:
        return False
    
    for i in range(len(ladybug_str) - 2):
        if ladybug_str[i] != ladybug_str[i + 1] and ladybug_str[i + 1] != ladybug_str[i + 2]:
            return False
        
    return True


def solve(b):
    all_space = all(c == '_' for c in b)
    if all_space:
        return True
    
    has_space = '_' in b
    count = collections.Counter(b)
    del count['_']
    less_common = count.most_common()[::-1][0]
    
    if (has_space and less_common[1] > 1) or (not has_space and are_happy(b)):
        return True
    return False
        

Q = int(input().strip())
for _ in range(Q):
    n = int(input().strip())
    b = input().strip()
    
    ans = solve(b)
    print("YES" if ans else "NO")