#!/bin/python3
import sys

s = input().strip()
nb_words = 1 + sum([c.isupper() for c in s])

print(nb_words)
