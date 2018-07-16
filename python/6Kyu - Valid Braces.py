# My Solution

def validBraces(string):
    parenthesis = []
    dict = {"{":"}", "[":"]", "(":")", "}":"{", "]":"[", ")":"("}
    
    for i in range(len(string)):
        if string[i] == "(" or string[i] == "[" or string[i] == "{":
            parenthesis.append(string[i])
        else :
            if len(parenthesis) == 0:
                return False
            elif dict[string[i]] == parenthesis[len(parenthesis)-1]:
                del parenthesis[len(parenthesis)-1]
            else:
                return False
            
    if len(parenthesis) != 0:
        return False
    return True
