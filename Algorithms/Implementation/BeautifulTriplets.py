#!/bin/python3
import sys


n, d = [int(_) for _ in input().strip().split(' ')]
A = {int(_) for _ in input().strip().split(' ')}

ans = sum([a + d in A and a + 2*d in A for a in A])
print(ans)
