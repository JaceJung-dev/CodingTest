def solution(sizes):
    answer = 0
    
    max_long = 0
    max_short = 0
    
    for size in sizes:
        long = max(size)
        short = min(size)
        
        max_long = max(max_long, long)
        max_short = max(max_short, short)
    
    answer = max_long * max_short
    
    return answer