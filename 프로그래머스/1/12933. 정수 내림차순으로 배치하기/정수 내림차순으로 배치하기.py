def solution(n):
    answer = 0
    n_str = sorted(str(n), reverse=True)
    answer = "".join(n_str)
    return int(answer)