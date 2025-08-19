def solution(l, r):
    answer = []
    except_num = ("1", "2", "3", "4", "6", "7", "8", "9")
    for num in range(l, r + 1):
        has_exception = False
        for n in str(num):
            if n in except_num:
                has_exception = True
                break
            
        if not has_exception:
            answer.append(num)
        
    if not answer:
        answer.append(-1)
            
    return answer