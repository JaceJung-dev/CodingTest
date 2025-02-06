def solution(numbers):
    answer = 0
    full_set = set(range(10))
    num_set = set(numbers)
    missing_num = full_set - num_set
    answer = sum(missing_num)
    return answer