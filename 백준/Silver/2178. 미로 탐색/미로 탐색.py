import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
maze = [input().strip() for _ in range(N)]
visited = [[False] * M for _ in range(N)]
dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
dist = [[0] * M for _ in range(N)]

queue = deque([(0, 0)])
visited[0][0] = True
dist[0][0] = 1

while queue:
    y, x = queue.popleft()

    if (y, x) == (N - 1, M - 1):
        print(dist[y][x])
        break

    for dx, dy in dirs:
        n_x, n_y = x + dx, y + dy

        if 0 <= n_y < N and 0 <= n_x < M:
            if not visited[n_y][n_x] and maze[n_y][n_x] == "1":
                queue.append((n_y, n_x))
                visited[n_y][n_x] = True
                dist[n_y][n_x] = dist[y][x] + 1
