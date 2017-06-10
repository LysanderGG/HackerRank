#!/bin/python3
import sys


def min_steps(n, B):
    return B.count("010")

n = int(input().strip())
B = input().strip()
result = min_steps(n, B)
print(result)
