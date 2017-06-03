#!/bin/python3
import sys


n,m = input().strip().split(' ')
n,m = [int(n),int(m)]
c = sorted(list(map(int, input().strip().split(' '))))

dist = [c[0], n - c[m - 1] - 1]
dist += [(c[i + 1] - c[i]) // 2 for i in range(m-1)]

ans = max(dist)
print(ans)
