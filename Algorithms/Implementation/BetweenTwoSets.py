#!/bin/python3
import sys

def getTotalX(a, b):
    return sum(
        (all(x % val_a == 0 for val_a in a) and 
         all(val_b % x == 0 for val_b in b))
        for x in range(1, min(b)+1))

n, m = input().strip().split(' ')
n, m = [int(n), int(m)]
a = list(map(int, input().strip().split(' ')))
b = list(map(int, input().strip().split(' ')))
total = getTotalX(a, b)
print(total)
