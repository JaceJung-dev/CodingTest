import sys
from collections import deque

sys.setrecursionlimit(10**6)

input = sys.stdin.readline


# Solution 1
def dfs(y, x, h):

    if not (0 <= y < N and 0 <= x < N):
        return

    if visited[y][x] or (matrix[y][x] <= h):
        return

    visited[y][x] = True

    for dy, dx in dirs:
        ny = y + dy
        nx = x + dx
        dfs(ny, nx, h)


def get_cc_count(height):
    global visited

    visited = [[False] * N for _ in range(N)]

    cc_count = 0
    for y in range(N):
        for x in range(N):
            if (not visited[y][x]) and (matrix[y][x] > height):
                dfs(y, x, height)
                cc_count += 1
    return cc_count


N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

max_cc_count = 0
for h in range(101):
    max_cc_count = max(max_cc_count, get_cc_count(h))

print(max_cc_count)

