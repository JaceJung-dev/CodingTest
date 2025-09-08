from collections import deque

def solution(priorities, location):
    # (우선순위, 위치) 형태의 queue / FIFO
    queue = deque([(priority, index) for index, priority in enumerate(priorities)])
    print(deque(list(enumerate(priorities))))
    answer = 0
    
    while queue:
        # 큐에서 프로세스 하나를 꺼냄
        cur = queue.popleft()
        
        # queue에 남아있는 다른 프로세스들과 비교
        for other in queue:
            # 현재 꺼낸 프로세스보다 우선순위 높은 것이 queue에 남아있는 경우
            if cur[0] < other[0]:
                queue.append(cur)
                break
        else:
            # 꺼낸 프로세스가 가장 높은 우선 순위인 경우
            answer += 1
            # 꺼낸 프로세스가 궁금해하던 프로세스이면 종료
            if cur[1] == location:
                break
                
    return answer