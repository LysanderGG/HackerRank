#!/bin/python3
import sys

dh = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve"
}
    
dm = {
    1: "one minute",
    2: "two minutes",
    3: "three minutes",
    4: "four minutes",
    5: "five minutes",
    6: "six minutes",
    7: "seven minutes",
    8: "eight minutes",
    9: "nine minutes",
    10: "ten minutes",
    11: "eleven minutes",
    12: "twelve minutes",
    13: "thirteen minutes",
    14: "forteen minutes",
    15: "quarter",
    16: "sixteen minutes",
    17: "seventeen minutes",
    18: "eighteen minutes",
    19: "nineteen minutes",
    20: "twenty minutes",
    21: "twenty one minutes",
    22: "twenty two minutes",
    23: "twenty three minutes",
    24: "twenty four minutes",
    25: "twenty five minutes",
    26: "twenty six minutes",
    27: "twenty seven minutes",
    28: "twenty eight minutes",
    29: "twenty nine minutes",
    30: "half"
}

h = int(input().strip())
m = int(input().strip())

if m == 0:
    s = dh[h] + " o' clock"
else:
    if m <= 30:
        s = dm[m] + " past " + dh[h]
    else:
        s = dm[60 - m] + " to " + dh[h + 1]
    
print(s)
