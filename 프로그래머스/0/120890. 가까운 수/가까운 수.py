def solution(array, n):
    answer = array[0]
    diff = abs(array[0] - n)
    for num in array:
        current_diff = abs(num - n)
        if current_diff < diff or (current_diff == diff and num < answer):
            diff = current_diff 
            answer = num

    return answer

