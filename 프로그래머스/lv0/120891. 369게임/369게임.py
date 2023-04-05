def solution(order):
    print(list((1 for i in range(0, len(str(order))) if order//(10**i) % 10 > 0 and order//(10**i) % 10 % 3 != 0)  ))
    return sum(1 for i in range(0, len(str(order))) if order//(10**i) % 10 > 0 and order//(10**i) % 10 % 3 == 0)  