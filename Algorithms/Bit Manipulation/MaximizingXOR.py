#!/usr/bin/python3
def maxXor(l, r):
    res = 0
    for a in range(l, r+1):
        for b in range(a, r+1) :
            res = max(res, a ^ b)
    return res

if __name__ == '__main__':
    l = int(input())
    r = int(input())
    print(maxXor(l, r))
