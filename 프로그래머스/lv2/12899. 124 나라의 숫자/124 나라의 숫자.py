def solution(n):
    answer = ""
    array = [1, 2, 4]
    while n > 0:
        n -= array[0]
        answer = str(array[(n % 3)]) + answer 
        n //= len(array)
    
    
    return answer