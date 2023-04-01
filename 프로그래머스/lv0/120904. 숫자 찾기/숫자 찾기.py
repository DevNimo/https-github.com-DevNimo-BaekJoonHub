def solution(num, k):
    response = str(num).find(str(k)) 
    return response + 1 if response != -1 else response