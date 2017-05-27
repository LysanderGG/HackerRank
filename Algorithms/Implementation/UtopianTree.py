#!/bin/python3

import sys

def grow(cycle):
    if cycle == 0:
        return 1
    elif cycle % 2 == 1:
        return 2 * grow(cycle - 1)
    else:
        return 1 + grow(cycle - 1)

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(grow(n))