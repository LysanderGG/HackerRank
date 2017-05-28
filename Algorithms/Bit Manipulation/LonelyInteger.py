#!/usr/bin/py

def lonelyinteger(b):
    bit_accumulator = 0
    for i in b:
        bit_accumulator ^= i
    return bit_accumulator

if __name__ == '__main__':
    a = int(input())
    b = map(int, input().strip().split(" "))
    print(lonelyinteger(b))
