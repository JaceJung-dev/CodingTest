def solution(strArr):
    len_list = [0] * 31
    answer = 0
    for char in strArr:
        len_list[len(char)] += 1
    answer = max(len_list)
    print(len_list)
    return answer