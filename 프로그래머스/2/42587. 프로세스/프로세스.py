from collections import deque

def solution(priorities, location):
    # (우선순위, 위치) 형태의 queue
    queue = deque([(priority, index) for index, priority in enumerate(priorities)])
    
    answer = 0
    
    while queue:
        cur = queue.popleft()
        
        for other in queue:
            if cur[0] < other[0]:
                queue.append(cur)
                break
        else:
            answer += 1
            if cur[1] == location:
                break
                
    return answer