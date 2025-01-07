def solution(arr, intervals):
    answer = []
    for idx in intervals:
        answer += arr[idx[0]:idx[1]+1]
    return answer