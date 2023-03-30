def solution(rsp):
    return "".join("0" if s == "2" else "5" if s == "0" else "2" for s in rsp)