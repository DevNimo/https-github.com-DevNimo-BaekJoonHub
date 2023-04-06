def solution(array, n):
    
    array.append(n)
    array.sort()
    index = array.index(n)
    arr_len = len(array)
    
    if not index:
        return array[index+1]
    if arr_len-1 == index:
        return array[index-1]
    st, lt = n - array[index-1] , array[index+1] - n
    return array[index-1] if st <= lt else array[index+1]
        