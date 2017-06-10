#!/bin/python3
import sys


def encrypt(s, k):
    res = ""
    for c in s:
        if c.isalpha():
            base = ord('A') if c.isupper() else ord('a')
            res += chr(base + (ord(c) - base + k) % 26)
        else:
            res += c
    return res
        
n = int(input().strip())
s = input().strip()
k = int(input().strip())
ans = encrypt(s, k)
print(ans)