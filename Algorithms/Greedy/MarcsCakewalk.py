#!/bin/python3
import sys


n = int(input().strip())
calories = list(map(int, input().strip().split(' ')))
calories.sort(reverse=True)

ans = 0
i = 0
for c in calories:
    ans += c * 2**i
    i += 1
    
print(ans)

