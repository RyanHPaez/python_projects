def solution(a):
    def get_sum(a, x):
        my_sum = 0
        for term in a:
            my_sum += abs(term-x)
        return my_sum

    all_sum = []
    for n,x in enumerate(a):
        all_sum.append(get_sum(a,x))
        if n > 1:
            if all_sum[n] > all_sum[n-1]:
                return a[all_sum.index(min(all_sum))]
    return a[all_sum.index(min(all_sum))]




print(solution([2, 4, 7]))