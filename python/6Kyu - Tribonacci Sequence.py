# My Solution

def tribonacci(signature, n):
    tribonacci = []
    
    for i in range(n):
        sequence = signature[-1] + signature[-2] + signature[-3]
        signature.append(sequence)
        new_sequence = signature.pop(0)
        tribonacci.append(new_sequence)
    return tribonacci
