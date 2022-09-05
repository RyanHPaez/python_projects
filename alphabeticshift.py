def solution(inputString):
    output = ""
    for letter in inputString:
        if letter == "z":
            output += "a"
        else:
            output += chr(ord(letter) + 1)
    return output