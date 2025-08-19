def solution(score):
    answer = []
    sum_score = [a + b for a, b in score]
    sum_score_sort = sorted(sum_score, reverse=True)
    
    for score in sum_score:
        rank = sum_score_sort.index(score) + 1
        answer.append(rank)
        
    return answer