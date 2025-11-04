import sys
from collections import deque

input = sys.stdin.readline

box = []
start_points = []
M, N = map(int, input().split())
for j in range(N):
    row = list(map(int, input().split()))
    box.append(row)
    for i in range(M):
        if row[i] == 1:
            start_points.append((j, i))

dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
queue = deque(start_points)

while queue:
    y, x = queue.popleft()

    for dx, dy in dirs:
        n_x, n_y = x + dx, y + dy

        if 0 <= n_x < M and 0 <= n_y < N:
            if box[n_y][n_x] == 0 and box[n_y][n_x] != -1:
                box[n_y][n_x] = box[y][x] + 1
                queue.append((n_y, n_x))


def get_day(box):
    max_day = -1
    for j in range(N):
        for i in range(M):
            max_day = max(max_day, box[j][i])
            if box[j][i] == 0:
                max_day = -1
                return max_day
    return max_day - 1


print(get_day(box))
