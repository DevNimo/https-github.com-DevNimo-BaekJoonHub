def solution(A, B):
    if A == B:
        return 0
    count = 0
    for i in range(len(A) - 1 , 0 , -1):
        count += 1
        if A[i:] + A[:i] == B:
            return count
    return - 1