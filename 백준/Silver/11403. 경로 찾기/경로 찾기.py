import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N)]

for i in range(N):
    row = list(map(int, input().split()))
    for j in range(N):
        if row[j] == 1:
            graph[i].append(j)

edge = [[0] * N for _ in range(N)]

for start in range(N):
    visited = [False] * N
    queue = deque([start])

    while queue:
        cur = queue.popleft()
        
        for next_node in graph[cur]:
            if not visited[next_node]:
                visited[next_node] = True
                queue.append(next_node)

    for end in range(N):
        edge[start][end] = 1 if visited[end] else 0

for row in edge:
    print(*row)