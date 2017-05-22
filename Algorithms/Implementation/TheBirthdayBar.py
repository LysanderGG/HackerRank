#!/bin/python3
import sys

def solve(n, s, d, m):
    return sum(sum(s[i:i+m]) == d for i in range(n - m + 1))

n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
d, m = input().strip().split(' ')
d, m = [int(d), int(m)]
result = solve(n, s, d, m)
print(result)
