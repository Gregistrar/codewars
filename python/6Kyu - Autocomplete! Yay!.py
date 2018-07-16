# My Solution

import string
import re
def autocomplete(input_, dictionary):
    input = ''.join(x for x in input_ if x.isalpha())
    results = []
    for i in dictionary:
        if i.lower().startswith(input.lower()):
            results.append(i)
    return results[0:5]
