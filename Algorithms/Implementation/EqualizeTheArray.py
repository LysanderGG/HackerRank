#!/bin/python3
from collections import Counter

n = input().strip()
a = list(map(int, input().strip().split(' ')))

res = len(a) - Counter(a).most_common(1)[0][1]
print(res)