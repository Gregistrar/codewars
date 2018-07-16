"""
Given two integers a and b, which can be positive or negative, find the sum of all the numbers between including them too and return it. If the two numbers are equal return a or b.

Note: a and b are not ordered!
"""


# My Solution

def get_sum(a,b):
    if a == b:
        return a
    s = 0
    for x in range(min(a,b), max(a,b)+1):
        s += x
    return s
