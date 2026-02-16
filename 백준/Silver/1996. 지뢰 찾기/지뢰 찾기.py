import sys

input = sys.stdin.readline

dirs = [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (-0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1),
]


def count_mine(i, j):
    count = 0
    for dx, dy in dirs:
        n_x, n_y = i + dx, j + dy

        if 0 <= n_x < N and 0 <= n_y < N:
            if mine[n_y][n_x] != ".":
                count += int(mine[n_y][n_x])
    return count


N = int(input())
mine = [input().strip() for _ in range(N)]

mine_map = [[""] * N for _ in range(N)]

for j in range(N):
    for i in range(N):
        if mine[j][i] != ".":
            mine_map[j][i] = "*"
        else:
            mine_counts = count_mine(i, j)
            if mine_counts >= 10:
                mine_map[j][i] = "M"
            else:
                mine_map[j][i] = str(mine_counts)

for row in mine_map:
    print("".join(row))
