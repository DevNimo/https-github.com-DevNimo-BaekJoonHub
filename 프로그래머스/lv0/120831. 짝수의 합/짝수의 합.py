def solution(n):
    return sum((num for num in range(0, n+1) if not num % 2))