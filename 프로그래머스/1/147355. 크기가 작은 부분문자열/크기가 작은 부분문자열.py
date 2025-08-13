def solution(t, p):
    answer = 0
    length = len(p)
    
    for i in range(0, len(t) - length + 1):
        if t[i:i+length] <= p:
            answer += 1
            
    return answer