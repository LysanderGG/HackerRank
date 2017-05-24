#!/bin/python3
import sys

n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]

max_set_size = 0

for unique_a in set(a):
    multiset = [k for k in a if 0 <= (k - unique_a) <= 1]
    max_set_size = max(max_set_size, len(multiset))

print(max_set_size)
