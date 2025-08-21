def solution(arr):
    answer = []
    if len(arr) == 1:
        answer.append(-1)
    else:
        min_num = min(arr)
        answer = [num for num in arr if num != min_num]
        
    return answer