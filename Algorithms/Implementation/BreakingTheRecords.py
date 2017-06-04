#!/bin/python3
import sys

def getRecord(s):
    nb_best_breaks = nb_worst_breaks = 0

    if len(s) > 0:
        best = worst = s[0]
        for score in s:
            if score > best:
                best = score
                nb_best_breaks += 1
            elif score < worst:
                worst = score
                nb_worst_breaks += 1
    
    return nb_best_breaks, nb_worst_breaks

n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
result = getRecord(s)
print (" ".join(map(str, result)))