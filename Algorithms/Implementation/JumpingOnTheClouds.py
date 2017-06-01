#!/bin/python3
import sys


n = int(input().strip())
c = [int(c_temp) for c_temp in input().strip().split(' ')]
i = 0
nb_jumps = 0

while i < len(c) - 3:
    i += 1 if c[i + 2] == 1 else 2
    nb_jumps += 1
    
print(nb_jumps + 1)