#!/bin/python3
import sys


def contains_word(s, word):
    for c in s:
        if c == word[0]:
            if len(word) == 1:
                return True
            word = word[1:]
    return False
    

q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    print("YES" if contains_word(s, "hackerrank") else "NO")
