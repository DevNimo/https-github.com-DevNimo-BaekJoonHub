def solution(quiz):
    return [["X", "O"][eval(s.split("=")[0]) == int(s.split("=")[1])] for s in quiz]