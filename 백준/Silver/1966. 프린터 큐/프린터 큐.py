import sys
from collections import deque

input = sys.stdin.readline


T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    priorities = list(map(int, input().split()))
    
    queue = deque([(priority, index) for index, priority in enumerate(priorities)])
    count = 0
    while queue:
        cur = queue.popleft()
        
        for doc in queue:
            if cur[0] < doc[0]:
                queue.append(cur)
                break
        else:
            count += 1

            if cur[1] == M:
                print(count)
                break
                
    