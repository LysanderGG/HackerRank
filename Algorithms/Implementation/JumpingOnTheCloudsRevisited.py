#!/bin/python3
import sys


n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
c = [int(c_temp) for c_temp in input().strip().split(' ')]
e = 100
curr = 0

while True:
    e -= 1
    curr = (curr + k) % n
    if c[curr] == 1:
        e -= 2
    
    if curr == 0:
        break
        
print(e)

