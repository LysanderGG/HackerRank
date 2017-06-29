#!/bin/python3
import sys


def is_valid(s):
    return len(s) > 1 and all(s[i] != s[i+1] for i in range(len(s) - 1))


def solve(s):
    chars = set(s)
    max_len = 0
    for c1 in chars:
        for c2 in chars:
            s12 = [c for c in s if c in (c1, c2)]
            if is_valid(s12):
                max_len = max(max_len, len(s12))
    return max_len
    
    
s_len = int(input().strip())
s = input().strip()
ans = solve(s)
print(ans)            
        