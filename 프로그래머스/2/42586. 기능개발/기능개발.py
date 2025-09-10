import math
from collections import deque


def solution(progresses, speeds):
    
    answer = []
    # (남은 일수, 원래 순서)
    queue = deque([(math.ceil((100 - progresses[i]) / speeds[i]) ,i) for i in range(len(progresses))])

    while queue:
        cur = queue.popleft()
        count = 1
        
        # 일괄처리(현재 선택된 작업보다 일찍 끝나는 작업들)된 것들 같이 카운팅
        while queue and queue[0][0] <= cur[0]:
            queue.popleft()
            count += 1
        
        # 한번 배포될 때 진행되는 작업 개수
        answer.append(count)
                
    return answer