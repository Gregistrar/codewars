# My Solution

def format_duration(seconds):
    year, day, hour, min = 0, 0, 0, 0
    unit, val = [], []
    y, d, h, m, s, res = " year", " day", " hour"," minute", " second", ""
    
    if seconds == 0:
        res = "now"
        
    while seconds >= 60:
        min += 1
        seconds -= 60
    while min >= 60:
        hour += 1
        min -= 60
    while hour >= 24:
        day += 1
        hour -= 24
    while day >= 365:
        year += 1
        day -= 365
    
    if year > 0:
        if year > 1:
            y += "s"
        unit.append(y)
        val.append(year)
    
    if day > 0:
        if day > 1:
            d += "s"
        unit.append(d)
        val.append(day)
    
    if hour > 0:
        if hour > 1:
            h += "s"
        unit.append(h)
        val.append(hour)
    
    if min > 0:
        if min > 1:
            m += "s"
        unit.append(m)
        val.append(min)
        
    if seconds > 0:
        if seconds > 1:
            s += "s"
        unit.append(s)
        val.append(seconds)
    
    x = len(unit) - 1
    
    while x >= 0:
        res = str(val[x]) + unit[x] + res
        if x == len(unit) -1 and len(unit) > 1:
            res = ' and ' + res
        elif x <= len(unit) - 2 and x > 0:
            res = ", " + res
        x -= 1
    return res
