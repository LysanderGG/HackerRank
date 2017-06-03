#!/bin/python3
import sys


N = int(input().strip())
B = [int(B_temp) for B_temp in input().strip().split(' ')]

res = 0
for i in range(len(B) - 1):
    if B[i] % 2 == 1:
        B[i] += 1
        B[i + 1] += 1
        res += 2

if B[-1] % 2 == 1:
    print("NO")
else:
    print(res)
        