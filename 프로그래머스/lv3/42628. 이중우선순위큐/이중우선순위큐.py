def solution(operations):
    answer = []
    for operation in operations:
        cmd_list = operation.split(" ")
        _oper , _v = cmd_list[0], int(cmd_list[1])
        if _oper == "I":
            answer.append(_v)
        elif answer:
            del answer[answer.index(max(answer) if _v > 0 else min(answer))]
    return [max(answer), min(answer)] if answer else [0,0]