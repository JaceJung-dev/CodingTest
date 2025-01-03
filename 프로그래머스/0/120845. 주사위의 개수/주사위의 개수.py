def solution(box, n):
    answer = 1
    for num in box:
        answer *= (num // n)
    return answer