import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

visited = [False] * (N + 1)
count = 0

for i in range(1, N + 1):
    if visited[i]:
        continue
    queue = deque([i])
    visited[i] = True

    while queue:
        cur = queue.popleft()
        visited[i] = True

        for node in graph[cur]:
            if not visited[node]:
                queue.append(node)
                visited[node] = True
    count += 1

print(count)
