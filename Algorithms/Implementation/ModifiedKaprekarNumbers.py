#!/bin/python3
import sys


def is_kaprekar(x):
    sq = str(x*x)
    l = int(sq[:len(sq) // 2]) if len(sq) > 1 else 0
    r = int(sq[len(sq) // 2:])
    return x == l + r


p = int(input().strip())
q = int(input().strip())

kaprekar = [x for x in range(p, q + 1) if is_kaprekar(x)]
if len(kaprekar) > 0:
    print(*kaprekar)
else:
    print("INVALID RANGE")
