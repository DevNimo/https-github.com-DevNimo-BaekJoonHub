def solution(n):
    for i in range(1, n//2):
        if i*i == n:
            return 1
    return 2 