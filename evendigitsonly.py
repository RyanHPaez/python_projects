def solution(n):
    for digit in str(n):
        if int(digit) % 2:
            return False
    return True

