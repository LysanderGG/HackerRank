#!/bin/python3
import sys

FINE_D = 15
FINE_M = 500
FINE_Y = 10000

d1,m1,y1 = list(map(int, input().strip().split(' ')))
d2,m2,y2 = list(map(int, input().strip().split(' ')))

if y1 == y2:
    if m1 == m2:
        fine = max(0, FINE_D * (d1 - d2))
    else:
        fine = max(0, FINE_M * (m1 - m2))
else:
    fine = FINE_Y if y1 > y2 else 0

print(fine)