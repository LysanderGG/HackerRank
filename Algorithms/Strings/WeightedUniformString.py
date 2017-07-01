#!/bin/python3
import sys

    
s = input().strip()
n = int(input().strip())
weights = set()

curr_c = s[0]
count = 0
for c in s:
    if curr_c != c:        
        count = 0
        curr_c = c
    count += ord(c) - ord('a') + 1
    weights.add(count)
        
for a0 in range(n):
    x = int(input().strip())
    print("Yes" if x in weights else "No")
