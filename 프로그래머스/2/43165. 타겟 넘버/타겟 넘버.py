def solution(numbers, target):
    answer = 0
    total_list = [0]
    for num in numbers:
        temp = []
        for total in total_list:
            temp.append(total + num)
            temp.append(total - num)
        total_list = temp
        
    answer = total_list.count(target)
    return answer