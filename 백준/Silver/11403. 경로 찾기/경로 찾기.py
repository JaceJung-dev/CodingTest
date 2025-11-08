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


def has_edge(start, end):
    visited = [False] * N
    queue = deque([start])
    visited[start] = True

    while queue:
        cur = queue.popleft()

        for next_node in graph[cur]:
            if next_node == end:
                return True

            if not visited[next_node]:
                queue.append(next_node)
                visited[next_node] = True

    return False


edge = []
for i in range(N):
    row = []
    for j in range(N):
        if has_edge(i, j):
            row.append(1)
        else:
            row.append(0)
    edge.append(row)

for row in edge:
    print(*row)
