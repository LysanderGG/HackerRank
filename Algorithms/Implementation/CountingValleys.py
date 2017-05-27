#!/bin/python3
import sys

def count_valleys(seq):
    current_level = 0
    nb_valleys = 0
    for e in seq:
        if current_level == 0 and e == -1:
            nb_valleys += 1
        current_level += e
    
    return nb_valleys

n = int(input().strip())
seq = input().strip()
seq = [1 if e == 'U' else -1 for e in seq] #1 for up -1 for down
print(count_valleys(seq))
