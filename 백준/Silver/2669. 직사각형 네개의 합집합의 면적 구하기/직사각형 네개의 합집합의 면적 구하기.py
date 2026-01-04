import sys

input = sys.stdin.readline

grid = [[0] * 101 for _ in range(101)]

for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())

    for x in range(x1, x2):
        for y in range(y1, y2):
            grid[y][x] = 1

area = 0
for row in grid:
    area += sum(row)

print(area)
