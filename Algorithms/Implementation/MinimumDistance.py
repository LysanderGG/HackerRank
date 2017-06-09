#!/bin/python3
import sys


n = int(input().strip())
A = [int(A_temp) for A_temp in input().strip().split(' ')]
dic = {}
dist_min = 1000000

for i in range(len(A)):
    a = A[i]
    if a in dic:
        dist_min = min(dist_min, i - dic[a])
    dic[a] = i
    
print(-1 if dist_min == 1000000 else dist_min)
