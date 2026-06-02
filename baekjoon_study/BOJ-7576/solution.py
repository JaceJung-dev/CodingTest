import sys
from collections import deque

INF = 10**12

input = sys.stdin.readline

# input
M, N = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

# solve
queue = deque()
time = [[INF] * M for _ in range(N)]

for y in range(N):
    for x in range(M):
        if matrix[y][x] == 1:
            queue.append((y, x))
            time[y][x] = 0

while queue:
    y, x = queue.popleft()

    nxts = [(y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)]

    for ny, nx in nxts:
        if not (0 <= ny < N and 0 <= nx < M):
            continue

        if time[ny][nx] <= time[y][x] + 1:
            continue

        if matrix[ny][nx] == -1:
            continue

        queue.append((ny, nx))
        time[ny][nx] = time[y][x] + 1

ans = -1
for y in range(N):
    for x in range(M):
        if matrix[y][x] != -1:
            ans = max(ans, time[y][x])

print(ans if ans != INF else -1)
