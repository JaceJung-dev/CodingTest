import sys

input = sys.stdin.readline

M, N = map(int, input().split())

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
dir_idx = 0

visited = [[False] * N for _ in range(M)]
y, x = 0, 0
visited[y][x] = True

filled = 1
total = M * N
count = 0

while filled < total:
    dy, dx = dirs[dir_idx]
    n_y = y + dy
    n_x = x + dx

    if 0 <= n_y < M and 0 <= n_x < N and not visited[n_y][n_x]:
        y, x = n_y, n_x
        visited[y][x] = True
        filled += 1
    else:
        dir_idx = (dir_idx + 1) % 4
        count += 1

print(count)