#!/bin/python3

import sys

def solve(grades):
    return [grade + 5 - grade % 5 if grade >= 38 and grade % 5 >= 3 else grade for grade in grades]

n = int(input().strip())
grades = []
grades_i = 0
for grades_i in range(n):
   grades_t = int(input().strip())
   grades.append(grades_t)
result = solve(grades)

for r in result:
    print(r)