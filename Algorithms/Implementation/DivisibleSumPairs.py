#!/bin/python3
import sys
import itertools

n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
a = list(map(int, input().strip().split(' ')))

nb_pairs = sum((x + y) % k == 0 for (x, y) in itertools.combinations(a, 2))
print(nb_pairs)    
