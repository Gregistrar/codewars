# My Solution

def make_valley(arr):
    arr.sort(reverse=True)
    left = []
    right = []
    for i in arr:
        if len(left) == len(right):
            left.append(i)
        else:
            right.append(i)
    right.sort()
    for i in right:
        left.append(i)
    return left
