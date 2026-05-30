import sys
from collections import deque

input = sys.stdin.readline

# input
N, M = map(int, input().split())
maze = ["0" * (M + 1)] + ["0" + input().strip() for _ in range(N + 1)]

# solve
visited = [[False] * (M + 1) for _ in range(N + 1)]

dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

queue = deque()
queue.append((1, 1, 1))
visited[1][1] = True

while queue:
    dist, y, x = queue.popleft()

    if y == N and x == M:
        print(dist)
        exit()

    for dy, dx in dirs:
        ny, nx = y + dy, x + dx

        if (
            (1 <= ny <= N and 1 <= nx <= M)
            and (not visited[ny][nx])
            and (maze[ny][nx] == "1")
        ):
            queue.append((dist + 1, ny, nx))
            visited[ny][nx] = True
