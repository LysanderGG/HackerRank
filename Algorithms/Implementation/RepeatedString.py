#!/bin/python3
import sys


s = input().strip()
n = int(input().strip())

l = len(s)
nb_a = (n // l) * s.count('a') + s[:n % l].count('a')
print(nb_a)