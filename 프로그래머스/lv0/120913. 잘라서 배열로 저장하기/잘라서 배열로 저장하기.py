import math
def solution(my_str, n):
    return [my_str[i*n:(i+1)*n] for i in range(0, math.ceil(len(my_str)/n))]