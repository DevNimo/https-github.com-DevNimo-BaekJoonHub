def solution(sides):
    sides.sort()
    result = (2,1)
    return result[sides[2] < sides[0] + sides[1]]