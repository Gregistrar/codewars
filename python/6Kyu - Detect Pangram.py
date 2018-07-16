"""
A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).

Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.
"""


# My Solution

import string

def is_pangram(s):
    s = s.lower()
    count = 0
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    phrase = ""
    for i in s:
        for x in alphabet:
            if i == x and x not in phrase:
                phrase += i
    for letter in phrase:
        for char in alphabet:
            if char == letter:
                count += 1
    if count == 26:
        return True
    else:
        return False
