#!/bin/python3
import sys

t = int(input().strip())
n_cycles = 3

while t > n_cycles:
    t -= n_cycles
    n_cycles *= 2

print(n_cycles - t + 1)