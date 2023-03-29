def solution(age):
    return "".join((chr(97+int(str(age)[i:i+1]))) for i in range(0, len(str(age))))