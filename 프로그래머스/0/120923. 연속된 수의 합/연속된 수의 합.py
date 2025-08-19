def solution(num, total):
    answer = []
    add = num - 1
    
    t_add = (add * (add + 1)) // 2
    n = (total - t_add) // num
    
    for i in range(num):
        answer.append(n + i)
    
    return answer