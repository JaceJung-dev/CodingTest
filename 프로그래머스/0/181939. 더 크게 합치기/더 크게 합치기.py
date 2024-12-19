def solution(a, b):
    answer = 0
    res1 = int(f'{a}{b}')
    res2 = int(f'{b}{a}')
    if res1 >= res2:
        answer = res1
    else:
        answer = res2
    return answer