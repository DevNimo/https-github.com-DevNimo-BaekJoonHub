def solution(num, total):
    div, mod = divmod(total, num)
    check_num = 0 if num % 2 else 1 
    sub = num//2 - check_num
    start = div - sub
    end = start + num    
    return [i for i in range(start, end)]       
