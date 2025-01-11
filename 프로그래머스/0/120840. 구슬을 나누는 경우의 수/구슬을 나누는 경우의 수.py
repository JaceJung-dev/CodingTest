def fact(n):
    if n <= 1:
        return 1
    else:
        return n * fact(n-1)
    
def solution(balls, share):
    answer = fact(balls) / (fact(balls - share) * fact(share))
    return answer