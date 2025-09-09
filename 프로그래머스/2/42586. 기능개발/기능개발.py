from collections import deque
import math

def solution(progresses, speeds):
    answer = []
    
    queue = deque([(math.ceil((100 - progresses[i]) / speeds[i]) ,i) for i in range(len(progresses))])

    while queue:
        cur = queue.popleft()
        count = 1
        
        while queue and queue[0][0] <= cur[0]:
            queue.popleft()
            count += 1
        
        answer.append(count)
                
    return answer