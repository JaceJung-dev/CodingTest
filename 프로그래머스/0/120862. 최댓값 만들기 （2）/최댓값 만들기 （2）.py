def solution(numbers):
    answer = 0
    multi_arr = []
    for idx1 in range(len(numbers)):
        for idx2 in range(idx1 + 1, len(numbers)):
            multi_arr.append(numbers[idx1] * numbers[idx2])
            
    answer = max(multi_arr)
    return answer