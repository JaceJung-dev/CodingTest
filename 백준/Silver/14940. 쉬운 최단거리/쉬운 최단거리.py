import sys
from collections import deque

input = sys.stdin.readline


def get_target_cord(N, M, maze):
    for j in range(N):
        for i in range(M):
            if maze[j][i] == 2:
                return (j, i)


N, M = map(int, input().split())

maze = [list(map(int, input().split())) for _ in range(N)]
dist_map = [[-1] * M for _ in range(N)]
dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

target = get_target_cord(N, M, maze)

queue = deque()
visited = [[False] * M for _ in range(N)]
y, x = target
queue.append((y, x))
visited[y][x] = True
dist_map[y][x] = 0

while queue:
    y, x = queue.popleft()

    for dy, dx in dirs:
        n_y, n_x = y + dy, x + dx

        if 0 <= n_y < N and 0 <= n_x < M:
            if maze[n_y][n_x] != 0 and not visited[n_y][n_x]:
                queue.append((n_y, n_x))
                dist_map[n_y][n_x] = dist_map[y][x] + 1
                visited[n_y][n_x] = True

for j in range(N):
    row = []
    for i in range(M):
        if maze[j][i] == 0:
            row.append(0)
        else:
            row.append(dist_map[j][i])

    print(*row)
