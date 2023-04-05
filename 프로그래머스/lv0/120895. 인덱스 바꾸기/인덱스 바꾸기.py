def solution(my_string, num1, num2):
    return "".join(my_string[num2] if i == num1
                   else my_string[num1] if i == num2
                   else my_string[i] for i in range(0, len(my_string)))