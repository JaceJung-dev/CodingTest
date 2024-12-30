def solution(arr, delete_list):
    answer = [num for num in arr if num not in delete_list]
    return answer