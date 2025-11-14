import sys
from collections import deque

input = sys.stdin.readline


def bfs(x, y, color, area, visited, dirs):
    queue = deque([])
    queue.append((y, x))
    visited[y][x] = True

    while queue:
        y, x = queue.popleft()

        for dx, dy in dirs:
            nx, ny = x + dx, y + dy

            if 0 <= nx < N and 0 <= ny < N:
                if not visited[ny][nx] and area[ny][nx] == color:
                    visited[ny][nx] = True
                    queue.append((ny, nx))


N = int(input())

color_area = []
weak_area = []
for _ in range(N):
    color_row = input().strip()
    weak_row = color_row.replace("G", "R")
    color_area.append(color_row)
    weak_area.append(weak_row)

color_visited = [[False] * N for _ in range(N)]
weak_visited = [[False] * N for _ in range(N)]

dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

color_count = 0
for j in range(N):
    for i in range(N):
        if not color_visited[j][i]:
            color = color_area[j][i]
            bfs(i, j, color, color_area, color_visited, dirs)
            color_count += 1

weak_count = 0
for j in range(N):
    for i in range(N):
        if not weak_visited[j][i]:
            color = weak_area[j][i]
            bfs(i, j, color, weak_area, weak_visited, dirs)
            weak_count += 1

print(color_count, weak_count)
