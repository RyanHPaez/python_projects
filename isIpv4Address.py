def solution(inputString):
    s = inputString.split('.')
    digit =[]
    if(len(inputString)<=15):
        for i in s:
            if i.isdigit():
                if((i=='00') | (i=='01')):
                    return False
                i=int(i)
                if(i>=0 and i<=255):
                   digit.append(True)
                else:
                   digit.append(False)
            else:
               return False
        if(len(digit)==4):
            return all(digit)
        else:
            return False
    else:
        return False

inputString = "172.16.254.1",
print(solution(inputString))