# My Solution

def solve(a,b):
    counter = []
    for i in b:
        number = a.count(i)
        counter.append(number)
    return counter
