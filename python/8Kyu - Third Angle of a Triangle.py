"""
You are given two angles (in degrees) of a triangle.

Write a function to return the 3rd.

Note: only positive integers will be tested.
"""


# My Solution

def other_angle(a, b):
    return 180 - (a+b)
