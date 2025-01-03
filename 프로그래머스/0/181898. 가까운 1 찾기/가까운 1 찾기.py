def solution(arr, idx):
    answer = -1
    for i, v in enumerate(arr):
        if i >= idx and v == 1:
            answer = i
            break
        
    return answer