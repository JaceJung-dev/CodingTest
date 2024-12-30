def solution(str_list, ex):
    answer = ''
    for char in str_list:
        if ex not in char:
            answer += char
        else:
            pass
            
    return answer