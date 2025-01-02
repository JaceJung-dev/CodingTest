def solution(n_str):
    answer = n_str
    for idx, value in enumerate(n_str):
        if value != "0":
            answer = n_str[idx:]
            break

    return answer