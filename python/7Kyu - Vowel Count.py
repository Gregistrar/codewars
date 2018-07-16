# My Solution

def getCount(inputStr):
    count = 0
    for i in inputStr:
        if i in ('a','e','i','o','u'):
            count += 1
    return count
