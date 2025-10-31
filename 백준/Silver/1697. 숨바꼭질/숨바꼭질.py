import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())
visited = [False] * 100001
dist = [0] * 100001


queue = deque([N])
visited[N] = True

while queue:
    cur = queue.popleft()
    
    if cur == K:
        break
    
    for i in range(3):
        if i % 3 == 0:
            new_pos = cur + 1
        elif i % 3 == 1:
            new_pos = cur - 1
        else:
            new_pos = cur * 2
        
        if 0 <= new_pos <= 100000:
            if not visited[new_pos]:
                queue.append(new_pos)
                visited[new_pos] = True
                dist[new_pos] = dist[cur] + 1

print(dist[K])