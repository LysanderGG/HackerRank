#!/bin/python3
import sys

t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    a = [int(a_temp) for a_temp in input().strip().split(' ')]
    nb_on_time = sum([i <= 0 for i in a])
    print("YES" if nb_on_time < k else "NO")