#!/bin/python3
import sys


def solve(a):
    sum_l = 0
    sum_r = sum(a[1:]) if len(a) > 1 else 0
    for i in range(1, len(a)):
        sum_l += a[i - 1]
        sum_r -= a[i]
        if sum_l == sum_r:
            break
            
    return sum_l == sum_r
        
    
T = int(input().strip())
for a0 in range(T):
    n = int(input().strip())
    a = list(map(int, input().strip().split(' ')))
    result = solve(a)
    print("YES" if result else "NO")
