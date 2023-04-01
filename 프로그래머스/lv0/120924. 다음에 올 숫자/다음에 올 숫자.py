def solution(common):
    num1, num2, num3 = common[0], common[1], common[2]
    sub1, sub2 = num2-num1, num3-num2
    
    return common[-1] * (sub2//sub1) if sub1 != sub2 else common[-1] + sub1