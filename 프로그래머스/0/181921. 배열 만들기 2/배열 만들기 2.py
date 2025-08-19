def solution(l, r):
    answer = []
    
    for num in range(l, r + 1):
        if not set(str(num)) - set(["0", "5"]):
            answer.append(num)
            
    if not answer:
        answer.append(-1)
        
    return  answer