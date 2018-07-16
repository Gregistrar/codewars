# My Solution

def toJadenCase(string):
    return ' '.join(word[0].upper() + word[1:] for word in string.split(' '))
