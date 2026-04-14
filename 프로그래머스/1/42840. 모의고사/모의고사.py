def solution(answers):
    answer = []
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    q_nums = len(answers)
    
    scores = [0, 0, 0]
    
    for i in range(q_nums):
        if answers[i] == p1[i % 5]:
            scores[0] += 1
        
        if answers[i] == p2[i % 8]:
            scores[1] += 1
            
        if answers[i] == p3[i % 10]:
            scores[2] += 1
            
    max_score = max(scores)
    for i in range(3):
        if scores[i] == max_score:
            answer.append(i + 1)
        
    answer.sort()
    
    return answer