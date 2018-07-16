# My Solution

def compute_depth(n):
    digits = []
    counter = 1
    while len(digits) < 10:
        mult = n * counter
        counter += 1
        dig = list(int(d) for d in str(mult))
        for i in dig:
            if i not in digits:
                digits.append(i)
    return counter - 1
