def solution(price):
    num = price//100000
    return price * 80 // 100 if num >= 5 else price * 90 // 100 if num >=3 else price * 95 // 100 if num >= 1 else price