#!/bin/python3
import sys

def solve(n, p):
    # Number or pages to turn from front: p / 2
    # Number of pages to turn from the end (n-p) +1 if there is only one page at the end / 2
    return min(p // 2, (n - p + (n % 2 == 0)) // 2)

n = int(input().strip())
p = int(input().strip())
result = solve(n, p)
print(result)
