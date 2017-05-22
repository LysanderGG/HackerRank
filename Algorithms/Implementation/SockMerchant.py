#!/bin/python3
import sys

n = int(input().strip())
c = [int(c_temp) for c_temp in input().strip().split(' ')]

dic = {}
for sock in c:
    if sock in dic:
        dic[sock] += 1
    else:
        dic[sock] = 1

nb_pairs = sum(nb // 2 for _, nb in dic.items())
print(nb_pairs)