"""
Your task is to create a function that does four basic mathematical operations.

The function should take three arguments - operation(string/char), value1(number), value2(number).
The function should return result of numbers after applying the chosen operation.
"""


# My Solution

def basic_op(operator, value1, value2):
    a = value1
    b = value2
    return {'+': a+b, '-': a-b, '*': a*b, '/': a/b}.get(operator)
