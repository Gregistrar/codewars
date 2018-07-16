# My Solution

def pattern(n):
    count = 1
    array = ["1"]
    if n < 1:
        return ""
    elif n == 1:
        return "1"
    while count < n:
        count += 1
        new = ["\n"]
        for i in range(count):
            new.append(count)
        news = ''.join(str(i) for i in new)
        array.append(news)
        
    return ''.join(array)
        
