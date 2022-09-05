def solution(inputArray):
    maximum = 0
    for i in range(len(inputArray) - 1):
        if max(inputArray[i], inputArray[i + 1]) -  min(inputArray[i], inputArray[i + 1]) > maximum:
            maximum = max(inputArray[i], inputArray[i + 1]) -  min(inputArray[i], inputArray[i + 1])
    return maximum