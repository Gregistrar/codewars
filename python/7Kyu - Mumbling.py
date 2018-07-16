# My Solution

def accum(s):
    array = []
    counter = 0
    for i in s:
        new = []
        a = 0
        new.append(i.upper())
        while a < counter:
            new.append(i.lower())
            a += 1
        new = ''.join(new)
        array.append(new)
        counter += 1
    return '-'.join(array)
