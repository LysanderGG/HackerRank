#!/bin/python3
import sys

def solve(year):
    if year == 1918:
        return "26.09.1918"
    
    if year < 1918:
        is_leap = year % 4 == 0
    else:
        # year > 1918
        is_leap = year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)
    dd = 12 if is_leap else 13
    return "{}.09.{}".format(dd, year)
        

year = int(input().strip())
result = solve(year)
print(result)
