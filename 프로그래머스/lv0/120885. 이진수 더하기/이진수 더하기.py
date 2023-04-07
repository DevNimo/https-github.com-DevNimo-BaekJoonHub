def solution(bin1, bin2):
    num1, num2 = 0, 0
    b1_len = len(bin1) - 1
    for b1 in bin1:
        num1 += 2 ** b1_len * int(b1)
        b1_len -= 1
    
    b2_len = len(bin2) - 1
    for b2 in bin2:
        num2 += 2 ** b2_len * int(b2)
        b2_len -= 1
    value = num1 + num2
    answer = ""
    while value:
        d, m = divmod(value,2)
        answer += str(m)
        value = d
    if "1" not in answer:
        return "0"
    return answer[::-1]