#!/bin/python3
import sys


n = int(input().strip())
p = list(map(int, input().strip().split(' ')))
p_dic = {p[i] : i + 1 for i in range(len(p))}

for i in range(1, n + 1):
    res = p_dic[p_dic[i]]
    print(res)
    