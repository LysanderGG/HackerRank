#!/bin/python3
import sys


t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    a = int(input().strip())
    b = int(input().strip())
    
    ans = sorted({a * i + b * (n - 1 - i) for i in range(n)})
    print(*ans)
