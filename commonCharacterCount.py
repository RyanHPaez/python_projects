from collections import Counter

def solution(s1, s2):
    return sum( min(s1.count(char), s2.count(char)) for char in (set(s1) & set(s2)))