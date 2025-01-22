def solution(s):
    answer = ''
    char_list = []
    for char in s:
        if s.count(char) == 1:
            char_list.append(char)
    
    char_list.sort()
    answer = "".join(char_list)
    return answer