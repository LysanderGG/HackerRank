#!/bin/python3
import sys


S = input().strip()
ans = sum("SOS"[i % 3] != S[i] for i in range(len(S)))
print(ans)