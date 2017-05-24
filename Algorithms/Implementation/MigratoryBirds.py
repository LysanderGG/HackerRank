#!/bin/python3
import sys

n = int(input().strip())
types = list(map(int, input().strip().split(' ')))

c = {i: 0 for i in range(1, 6)}
for t in types:
    c[t] += 1
    
max_type = max(c, key=c.get)
print(max_type)
