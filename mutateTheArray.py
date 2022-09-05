a = [4, 0, 1, -2, 3]
n = 5

def solution(n, a):
    if len(a) < 2:
        return a
    result = []
    for i in range(len(a)):
        # if i = 0 then i - 1 does not exist so [i-1] becomes 0 and we can
        # just leave it off
        if i == 0:
            result.append(a[i] + a[i + 1])
        # if i is pointing to the last element then [i + 1] does not exist so
        # it becomes 0 and we can just leave that off
        elif i == len(a) - 1:
            result.append((a[i - 1] + a[i]))
        # for all other cases just do the normal equation
        else:
            result.append(a[i - 1] + a[i] + a[i + 1])

    return result

print(solution(n, a))

# def solution(n, a):
#     b = a
    
#     for i in range(n):
#         print(i)
#         if i <= 0:
#             i = 0
            
#         else:
#             if i < n -1:
#                 b[i] = a[i-1] + a[i] + a[i + 1]
#     return b