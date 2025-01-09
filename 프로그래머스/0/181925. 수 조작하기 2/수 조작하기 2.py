def solution(numLog):
    answer = ''
    log_dict = {1: "w",
                -1: "s",
                10: "d",
                -10: "a"}

    for i in range(1, len(numLog)):
        diff_value = numLog[i] - numLog[i - 1]
        if diff_value in log_dict:
            answer += log_dict[diff_value]

    return answer