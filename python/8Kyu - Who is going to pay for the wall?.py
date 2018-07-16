# My Solution

def who_is_paying(name):
    array = [name]
    if name[0:2] == name:
        return array
    return [name, name[0:2]]
