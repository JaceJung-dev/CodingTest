def solution(nums):
    answer = 0
    n = len(nums)
    cleaned_n = len(set(nums))
    
    if cleaned_n >= n // 2:
        answer = n // 2
    else:
        answer = cleaned_n
    
    return answer