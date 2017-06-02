#!/bin/python3
import sys


if __name__ == "__main__":
    n = int(input().strip())

    n_likes = 2
    n_likes_i = 2
    for _ in range(n - 1):
        n_likes_i = (n_likes_i * 3) // 2
        n_likes += n_likes_i

    print(n_likes)
    