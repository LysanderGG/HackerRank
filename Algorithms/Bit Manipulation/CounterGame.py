#!/usr/bin/python3

# There is no need to apply the operations on x
# Just count the number of necessary operations
# Number of 1s before the last 1 and 0s after the last 1
# Equivalent to count the number of 1s in x-1
def solve(x):
    nb_turns = bin(x-1).count("1")
    return "Louise" if nb_turns & 1 else "Richard"

if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        t = int(input())
        print(solve(t))
