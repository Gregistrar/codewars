# My Solution

def get_digits(num, digits=[]):
    while num > 0:
        digits.append(num % 10)
        return get_digits(num/10, digits)
    if num == 0:
        return digits

def multiply(digits, mult=1):
    while len(digits) > 0:
        mult = mult * digits.pop(0)
        return multiply(digits, mult)
    if len(digits) == 0:
        return mult

def persistence(num, count=0):
    while num >= 10:
        num = multiply(get_digits(num))
        count += 1
    if num < 10:
        return count
