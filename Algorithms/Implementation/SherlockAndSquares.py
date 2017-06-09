#!/bin/python3
import sys
import math


def nb_primes_between(a, b):
    sa = math.ceil(math.sqrt(a))
    sb = math.floor(math.sqrt(b))
    return sb - sa + 1

    
t = int(input().strip())
for _ in range(t):
    a, b = list(map(int, input().strip().split(' ')))
    ans = nb_primes_between(a, b)
    print(ans)
