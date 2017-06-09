#!/bin/python3
import sys

def saveThePrisoner(n, m, s):
    return 1 + (s - 1 + m - 1) % n

t = int(input().strip())
for a0 in range(t):
    n, m, s = input().strip().split(' ')
    n, m, s = [int(n), int(m), int(s)]
    result = saveThePrisoner(n, m, s)
    print(result)
