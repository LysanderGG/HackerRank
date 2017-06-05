#!/bin/python3
import sys


n = int(input().strip())
grid = []
for _ in range(n):
   grid.append([int(c) for c in input().strip()])

print("".join([str(g) for g in grid[0]]))
for i in range(1, n-1):
    print(grid[i][0], end='')
    for j in range(1, n-1):
        g = int(grid[i][j])
        l = int(grid[i - 1][j])
        r = int(grid[i + 1][j])
        t = int(grid[i][j - 1])
        b = int(grid[i][j + 1])
        if all(g > a for a in (l, r, t, b)):
            print('X', end='')
        else:
            print(g, end='')
    print(grid[i][n - 1])
    
if n > 1:    
    print("".join([str(g) for g in grid[n - 1]]))