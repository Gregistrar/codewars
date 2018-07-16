"""
Write function parseFloat (for Javascript parseF) which takes a string and returns a number or Nothing 
(for Python None, for Javascript null) if conversion is not possible.
"""


# My Solution

def parse_float(string):
    try:
        float(string)
        return float(string)
    except:
        None
