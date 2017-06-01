#!/bin/python3
import sys


if __name__ == "__main__":
    h = list(map(int, input().strip().split(' ')))
    word = input().strip()

    max_h = max([h[ord(c) - ord('a')] for c in word])
    area = max_h * len(word)

    print(area)
    