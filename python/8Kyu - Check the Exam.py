# My Solution

def check_exam(arr1,arr2):
    score = 0
    counter = 0
    while counter < len(arr1):
        if arr1[counter] == arr2[counter]:
            score += 4
        elif arr2[counter] == "":
            score += 0
        elif arr1[counter] != arr2[counter]:
            score -= 1
        counter += 1
    if score < 0:
        return 0
    else:
        return score
