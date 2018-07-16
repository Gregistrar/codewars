# My Solution

def elevator_distance(array):
    return sum([abs(x[1]-x[0]) for x in zip(array[1:],array[:-1])])
