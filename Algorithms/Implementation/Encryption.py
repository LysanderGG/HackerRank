#!/bin/python3
import sys
import math


def encode(s):
    e = ""
    rows = int(math.sqrt(len(s)))
    cols = int(math.ceil(math.sqrt(len(s))))
    if rows * cols < len(s):
        rows = cols
    
    r, c = 0, 0
    for i in range(len(s)):
        idx = r * cols + c
        #print(idx)
        e += s[idx]
        r = r + 1
        if r * cols + c >= len(s):
            e += ' '
            r = 0
            c += 1
        
    return e

s = input().strip().replace(' ', '')
ans = encode(s)
print(ans)