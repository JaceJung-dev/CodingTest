def solution(land):
    answer = 0
    
    for i in range(1, len(land)):
        c0, c1, c2, c3 = land[i - 1]
        
        land[i][0] += max(c1, c2, c3)
        land[i][1] += max(c0, c2, c3)
        land[i][2] += max(c0, c1, c3)
        land[i][3] += max(c0, c1, c2)
    
    answer = max(land[-1])
    
    return answer