import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

relationship = [[] for _ in range(N + 1)]

for _ in range(M):
    f1, f2 = map(int, input().split())
    relationship[f1].append(f2)
    relationship[f2].append(f1)


def bfs(start):
    visited = [False] * (N + 1)
    dist = [0] * (N + 1)
    queue = deque([start])
    visited[start] = True

    while queue:
        cur = queue.popleft()
        for friend in relationship[cur]:
            if not visited[friend]:
                queue.append(friend)
                dist[friend] = dist[cur] + 1
                visited[friend] = True
    return sum(dist)


bacon_nums = [0] * (N + 1)
for i in range(1, N + 1):
    bacon_nums[i] = bfs(i)

min_index, min_num = 0, float("inf")

for i in range(1, N + 1):
    if bacon_nums[i] < min_num:
        min_num = bacon_nums[i]
        min_index = i

print(min_index)