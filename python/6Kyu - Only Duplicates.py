"""
Given a string, remove any characters that are unique from the string.

Example:

input: "abccdefee"

output: "cceee"
"""


# My Solution

def only_duplicates(string):
    
    new_word = []
    
    for i in string:
        if string.count(i) > 1:
            new_word.append(i)
    
    final = ''.join(new_word)
    
    return final
