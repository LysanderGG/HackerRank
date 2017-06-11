#!/bin/python3
import sys

def gemstones(arr):
    gem_set = set(arr[0])
    if len(arr) > 1:
        for a in arr[1:]:
            gem_set = gem_set & set(a)
    return len(gem_set)

n = int(input().strip())
arr = []
for _ in range(n):
    arr.append(str(input().strip()))
    
result = gemstones(arr)
print(result)
