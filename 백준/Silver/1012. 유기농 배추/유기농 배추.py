import sys
from collections import deque

input = sys.stdin.readline


def bfs(start_x, start_y, grid, visited):
    queue = deque([(start_x, start_y)])
    visited[start_y][start_x] = True

    while queue:
        x, y = queue.popleft()

        for dx, dy in dirs:
            new_x, new_y = x + dx, y + dy

            if 0 <= new_x < M and 0 <= new_y < N:
                if not visited[new_y][new_x] and grid[new_y][new_x] == 1:
                    queue.append((new_x, new_y))
                    visited[new_y][new_x] = True


dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())
    grid = [[0] * M for _ in range(N)]

    for _ in range(K):
        x, y = map(int, input().split())
        grid[y][x] = 1

    visited = [[False] * M for _ in range(N)]

    worms = 0
    for j in range(N):
        for i in range(M):
            if grid[j][i] == 1 and not visited[j][i]:
                bfs(i, j, grid, visited)
                worms += 1

    print(worms)
