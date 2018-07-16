# My Solution

def compound_match(words, target):
    for x in range(1, len(target)-1):
        first = target[:x]
        second = target[x:]
        if (first in words) and (second in words):
            uno = words.index(first)
            dos = words.index(second)
            return ([first, second] if uno < dos else [second, first]) +[[uno, dos]]
