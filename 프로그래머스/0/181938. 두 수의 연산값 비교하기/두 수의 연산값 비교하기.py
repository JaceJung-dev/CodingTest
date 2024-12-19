def solution(a, b):
    answer = 0
    cal_result = int(str(a) + str(b))
    if cal_result >= 2 * a * b:
        answer = cal_result
    else:
        answer = 2 * a * b
    return answer