# My Solution

def disemvowel(string):
    str = []
    for i in string:
        if i not in "aeiouAEIOU":
            str.append(i)
    return ''.join(str)
