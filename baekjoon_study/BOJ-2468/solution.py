import sys
from collections import deque

sys.setrecursionlimit(10**6)

input = sys.stdin.readline


# Solution 1
def dfs(sy, sx, height):

    if not (0 <= sy < N and 0 <= sx < N):
        return

    if visited[sy][sx] or (matrix[sy][sx] <= height):
        return

    visited[sy][sx] = True

    for dy, dx in dirs:
        ny, nx = sy + dy, sx + dx
        dfs(ny, nx, height)


def get_count(height):
    global visited

    visited = [[False] * N for _ in range(N)]

    count = 0
    for y in range(N):
        for x in range(N):
            if (not visited[y][x]) and (matrix[y][x] > height):
                dfs(y, x, height)
                count += 1
    return count


# input
N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

# solve
dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

max_count = 0
for h in range(101):
    max_count = max(max_count, get_count(h))

print(max_count)


# Solution 2
def bfs(sy, sx, height):
    queue = deque()
    queue.append((sy, sx))
    visited[sy][sx] = True

    while queue:
        y, x = queue.popleft()

        for dy, dx in dirs:
            ny, nx = y + dy, x + dx

            if (
                (0 <= nx < N and 0 <= ny < N)
                and (not visited[ny][nx])
                and (matrix[ny][nx] > height)
            ):
                queue.append((ny, nx))
                visited[ny][nx] = True


def get_count(height):
    global visited

    visited = [[False] * N for _ in range(N)]

    count = 0
    for y in range(N):
        for x in range(N):
            if (not visited[y][x]) and (matrix[y][x] > height):
                bfs(y, x, height)
                count += 1

    return count


# input
N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

# solve
dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

max_count = 0
for h in range(101):
    max_count = max(max_count, get_count(h))

print(max_count)
