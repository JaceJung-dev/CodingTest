def solution(arr):
    len_arr = len(arr)
    if len_arr & (len_arr-1) == 0:
        return arr

    next_power = 1
    while next_power < len_arr:
        next_power *= 2
        
    return arr + [0] * (next_power - len_arr)