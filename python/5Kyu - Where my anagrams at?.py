# My Solution

def anagrams(word, words):
    
    array = []
    new_word = ''.join(sorted(word))
    
    for string in words:
        order_word = ''.join(sorted(string))
        if order_word == new_word:
            array.append(string)
    return array
