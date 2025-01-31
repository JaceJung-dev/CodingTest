def solution(a, b):
    answer = 0
    if a == b:
        answer = a
    else:
        answer = sum([num for num in range(min(a,b), max(a,b)+1)])
    return answer