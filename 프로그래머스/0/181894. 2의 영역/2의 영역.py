def solution(arr):
    idx_list = []
    for i in range(len(arr)):
        if arr[i] == 2:
            idx_list.append(i)
            
    if not idx_list:
        return [-1]
    
    answer = arr[idx_list[0]: idx_list[-1] + 1]
    return answer