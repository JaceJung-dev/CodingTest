def get_count(num):
    count = 0
    while num != 1:
        count += 1
        if num % 2 == 0:
            num /= 2
        else:
            num = (num - 1) / 2
    return count

def solution(num_list):
    answer = 0
    for num in num_list:
        answer += get_count(num)
    return answer