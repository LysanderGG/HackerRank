#!/usr/bin/python3

def reverse(x):
    return int(str(x)[::-1])


def is_beautiful(x, k):
    return abs(x - reverse(x)) % k == 0


if __name__ == '__main__':
    i, j, k = map(int, input().strip().split(' '))
    res = sum(is_beautiful(day, k) for day in range(i, j + 1))
    print(res)
    