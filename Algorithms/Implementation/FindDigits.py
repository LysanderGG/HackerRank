#!/bin/python3
import sys

def find_digits(n):
    ans = 0
    for i in [int(char) for char in str(n)]:
        if i > 0 and n % i == 0:
            ans += 1
    return ans


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(find_digits(n))
    
    