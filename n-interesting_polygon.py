def solution(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    for i in range(2, n+1):
        return (solution(n-1) + (n-1)*4)