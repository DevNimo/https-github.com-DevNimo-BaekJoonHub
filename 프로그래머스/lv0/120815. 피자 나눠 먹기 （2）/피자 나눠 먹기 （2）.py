
def lcm(num1, num2):
    max_num = max([num1, num2])
    min_num = min([num1, num2])
    i = 1
    while True:
        if not (i * max_num) % min_num:
            return i * max_num
        i += 1

def solution(n):
    return lcm(n, 6) // 6