def solution(n):
    answer = 0
    
    for _ in range(n):
        answer += 1
        
        while True:
            if answer % 3 == 0 or "3" in str(answer):
                answer += 1
            else:
                break

    return answer