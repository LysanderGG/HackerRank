#!/bin/python3

import sys


s,t = input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = input().strip().split(' ')
a,b = [int(a),int(b)]
m,n = input().strip().split(' ')
m,n = [int(m),int(n)]
apple = [int(apple_temp) for apple_temp in input().strip().split(' ')]
orange = [int(orange_temp) for orange_temp in input().strip().split(' ')]

nb_apples_on_house = sum([s <= a + d <= t for d in apple])
nb_oranges_on_house = sum([s <= b + d <= t for d in orange])

print(nb_apples_on_house)
print(nb_oranges_on_house)