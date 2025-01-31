def solution(n):
    answer = 0
    n_sqrt = n ** 0.5
    if n_sqrt.is_integer():
        answer = (n_sqrt + 1) ** 2
    else:
        answer = -1

    return answer