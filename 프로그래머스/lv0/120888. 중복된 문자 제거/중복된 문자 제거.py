def solution(my_string):
    my_list = []
    for s in my_string:
        if s in my_list:
            continue
        my_list.append(s)

    return "".join(my_list)