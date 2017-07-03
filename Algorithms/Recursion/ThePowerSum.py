#!/usr/bin/python3
import math

def solve_rec(x, pow_integers, nb_sums, visited_states):
    state = frozenset(pow_integers)
    if state in visited_states:
        return 0
    visited_states.add(state)
    
    if x == 0:
        return 1 + nb_sums
    
    for i in range(len(pow_integers)):
        curr_int = pow_integers[i]
        if curr_int <= x:
            new_pow_integers = pow_integers[:i] + pow_integers[i+1:]
            nb_sums += solve_rec(x - curr_int, new_pow_integers, 0, visited_states)
        else:
            # pow_integers is sorted
            break
    
    return nb_sums

def solve(x, n):
    integers = [i for i in range(1, math.ceil(x ** (1. / n)) + 1)]
    pow_integers = [i ** n for i in integers]

    nb_sums = solve_rec(x, pow_integers, 0, set())
    return nb_sums

if __name__ == '__main__':
    x = int(input())
    n = int(input())
    print(solve(x, n))
