# My Solution

def race(v1, v2, g):
    if v1 >= v2:
        return None
    
    res = 3600*g//(v2-v1)
    return [res//60//60, res//60%60, res%60]
