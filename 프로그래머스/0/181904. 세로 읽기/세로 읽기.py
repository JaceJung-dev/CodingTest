def solution(my_string, m, c):
    str_list = my_string[c-1::m]
    answer = "".join(str_list)
    return answer