# My Solution

def convert(input, source, target):
    value = string_to_value(input, source)
    return value_to_string(value, target)
    
def string_to_value(input, encoding):
    n = len(encoding)
    result = 0
    for i in input:
        result = result * n + encoding.find(i)
    return result

def value_to_string(value, encoding):
    if not value:
        return encoding[0]
    n = len(encoding)
    result = []
    while value > 0:
        result.append(encoding[value % n])
        value //= n
    return ''.join(result[::-1])
