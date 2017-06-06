#!/bin/python3
import sys


n,k,q = list(map(int, input().strip().split(' ')))
a = list(map(int, input().strip().split(' ')))
for _ in range(q):
    m = int(input().strip())
    ans = a[(m - k) % n]
    print(ans)