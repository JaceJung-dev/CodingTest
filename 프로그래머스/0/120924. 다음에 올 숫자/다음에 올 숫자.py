def is_arithmetic(num_list):
    common_num = num_list[1] - num_list[0]
    for i in range(1, len(num_list) - 1):
        if common_num != num_list[i+1] - num_list[i]:
        	return False
    return True

def is_geometric(num_list):
    common_num = num_list[1] // num_list[0]
    for i in range(1, len(num_list) - 1):
        if common_num != num_list[i+1] // num_list[i]:
            return False
    return True

def solution(common):
    answer = 0
    if is_arithmetic(common):
        common_num = common[1] - common[0]
        answer = common[0] + common_num * len(common)
    else:
        common_num = common[1] // common[0]
        answer = common[0] * (common_num ** len(common))
    return answer