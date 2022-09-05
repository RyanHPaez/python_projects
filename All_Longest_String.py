def solution(inputArray): 
    m = len(max(inputArray, key=len))
    return [s for s in inputArray if len(s) ==m]