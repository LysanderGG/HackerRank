#!/bin/python3

n, k = map(int, input().strip().split(' '))
prices = list(map(int, input().strip().split(' ')))
paid_price = int(input().strip())

prices.pop(k)
fair_split = sum(prices) // 2
if paid_price == fair_split:
    print("Bon Appetit")
else:
    print(paid_price - fair_split)
	