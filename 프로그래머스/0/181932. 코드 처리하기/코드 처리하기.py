def solution(code):
    answer = ''
    mode = 0
    for idx, value in enumerate(code):
        if mode == 0:
            if value != '1' and idx % 2 == 0:
                answer += value
            if value == '1':
                mode = 1
        else:
            if value != '1' and idx % 2 == 1:
                answer += value
            if value == '1':
                mode = 0
    return answer if answer else "EMPTY"