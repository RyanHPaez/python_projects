def solution(inputArray, elemToReplace, substitutionElem):
    c=[]
    for k in inputArray:
        if k == elemToReplace:
            c.append(substitutionElem)
        else:
            c.append(k)
    return(c)
