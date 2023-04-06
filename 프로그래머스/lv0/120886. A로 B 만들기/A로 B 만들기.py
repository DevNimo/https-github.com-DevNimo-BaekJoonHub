def solution(before, after):
    return (0,1)[sorted(before) == sorted(after)]