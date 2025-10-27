import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
campus = []
start = None

for j in range(N):
    row = input().strip()
    campus.append(row)
    for i in range(M):
        if row[i] == "I":
            start = (j, i)

dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
visited = [[False] * M for _ in range(N)]

s_y, s_x = start
queue = deque([(s_y, s_x)])
visited[s_y][s_x] = True

friends = 0
while queue:
    y, x = queue.popleft()

    if campus[y][x] == "P":
        friends += 1

    for dy, dx in dirs:
        n_y, n_x = y + dy, x + dx

        if 0 <= n_y < N and 0 <= n_x < M:
            if campus[n_y][n_x] != "X" and not visited[n_y][n_x]:
                queue.append((n_y, n_x))
                visited[n_y][n_x] = True

if not friends:
    print("TT")
else:
    print(friends)
