#!/bin/python3
import sys
import bisect


n = int(input().strip())
scores = sorted(set(int(scores_temp) for scores_temp in input().strip().split(' ')))
m = int(input().strip())
alice = [int(alice_temp) for alice_temp in input().strip().split(' ')]

#Note: we could improve this by remembering the last i_score found.
for a in alice:
    i_score = bisect.bisect_right(scores, a) 
    print(len(scores) - i_score + 1)
    