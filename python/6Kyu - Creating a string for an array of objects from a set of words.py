# My Solution

def words_to_object(s):
    if s == '':
        return '[]'
    s = s.split()
    array = []
    counter = 0
    while counter < len(s):
        if len(s) == 2:
            array.append("[{name : '"+s[counter]+"', id : '"+s[counter+1]+"'}]")
        elif counter == 0:
            array.append("[{name : '"+s[counter]+"', id : '"+s[counter+1]+"'}")
        elif (counter+2) == len(s):
            array.append("{name : '"+s[counter]+"', id : '"+s[counter+1]+"'}]")
        else:
            array.append("{name : '"+s[counter]+"', id : '"+s[counter+1]+"'}")
        counter += 2
    new = ', '.join(array)
    return new
