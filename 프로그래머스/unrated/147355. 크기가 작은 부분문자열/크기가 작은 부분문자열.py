def solution(t, p):
    p_len = len(p)
    answer = 0
    for i in range(0,len(t)):
        target = t[i:i+p_len]
        if len(target) < p_len:
            break
        if int(p) >= int(target):
            answer+=1
    return answer