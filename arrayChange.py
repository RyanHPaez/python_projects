def solution(inputArray):
    output =0
    for i in range(len(inputArray) -1):
        if inputArray[i] >=inputArray[ i+1]:
            output += inputArray[i]-inputArray[i+1]+1
            inputArray[i+1] += inputArray[i] - inputArray[i +1] +1
    return output        

