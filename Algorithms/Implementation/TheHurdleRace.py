#!/bin/python3
import sys

n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
height = list(map(int, input().strip().split(' ')))

max_height = max(height)
nb_potions_to_drink = max(max_height - k, 0)
print(nb_potions_to_drink)