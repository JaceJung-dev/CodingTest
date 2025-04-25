def solution(arr, k):
    answer = []
    unique_list = []
    for num in arr:
        if num not in unique_list:
            unique_list.append(num)
    
    if len(unique_list) >= k:
        answer = unique_list[0:k]
    else:
        answer = unique_list + [-1] * (k-len(unique_list))
    return answer