def solution(inputArray):
    output = 2
    condition = True
    while condition:
        for number in inputArray:
            if number % output == 0:
                break
        if number % output != 0:
            condition = False
            break
        output += 1
    return output