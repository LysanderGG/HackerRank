#!/bin/python3
import sys


t = int(input().strip())
for _ in range(t):
    n,c,m = input().strip().split(' ')
    n,c,m = [int(n),int(c),int(m)]

    chocos = n // c
    wrappers = chocos
    while(wrappers >= m):
        new_chocos = wrappers // m
        wrappers = (wrappers % m) + new_chocos
        chocos += new_chocos
    
    print(chocos)