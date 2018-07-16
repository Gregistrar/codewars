# My Solution

import re
def decipher_this(string):
    array = string.split()
    new = []
    for i in array:
        letter = i.lstrip('0123456789')
        num = i.rstrip('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
        if len(letter) > 1:
            mid = letter[1:-1]
            whole = letter[-1:] + mid + letter[:1]
        else:
            whole = letter
        char = str(chr(int(num)))
        new.append(char+whole)
    return ' '.join(new)
