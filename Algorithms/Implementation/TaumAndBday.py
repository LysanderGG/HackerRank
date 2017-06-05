#!/bin/python3
import sys


t = int(input().strip())
for a0 in range(t):
    b,w = input().strip().split(' ')
    b,w = [int(b),int(w)]
    x,y,z = input().strip().split(' ')
    x,y,z = [int(x),int(y),int(z)]

    ans = min(
        b * x + w * y,
        b * min(x, y + z) + w * min(x + z, y)
    )
    print(ans)
