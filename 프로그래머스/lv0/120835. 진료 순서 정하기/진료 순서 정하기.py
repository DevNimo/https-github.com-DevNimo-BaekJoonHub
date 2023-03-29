def solution(emergency):
    
    return [len(emergency) - emergency.index(v) for v in sorted(emergency)]