from collections import Counter
def solution(array):
    result_tuple_list = Counter(array).most_common(2)
    return_key, check_val = result_tuple_list[0]
    length = len(result_tuple_list)
    if length > 1:
        if check_val == result_tuple_list[1][1]:
            return -1
        return return_key
        
    return return_key