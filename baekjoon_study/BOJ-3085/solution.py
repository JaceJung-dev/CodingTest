import sys

input = sys.stdin.readline

# Solution 1


def get_best():
    best = 0

    # rows
    for i in range(N):
        value = 0
        prev = "-"
        for j in range(N):
            if matrix[i][j] == prev:
                value += 1
            else:
                value = 1
            best = max(best, value)
            prev = matrix[i][j]

    # column
    for j in range(N):
        value = 0
        prev = "-"
        for i in range(N):
            if matrix[i][j] == prev:
                value += 1
            else:
                value = 1
            best = max(best, value)
            prev = matrix[i][j]

    return best


# input
N = int(input())
matrix = [list(input().strip()) for _ in range(N)]

# solve
dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

best = 0
for y in range(N):
    for x in range(N):
        for dy, dx in dirs:
            ny, nx = y + dy, x + dx

            if 0 <= ny < N and 0 <= nx < N:
                matrix[y][x], matrix[ny][nx] = matrix[ny][nx], matrix[y][x]
                best = max(best, get_best())
                matrix[y][x], matrix[ny][nx] = matrix[ny][nx], matrix[y][x]

print(best)

# Solution 2


def get_best(y, x):
    best = 0

    # row
    value = 0
    prev = "-"
    for j in range(N):
        if matrix[y][j] == prev:
            value += 1
        else:
            value = 1
        best = max(best, value)
        prev = matrix[y][j]

    # column
    value = 0
    prev = "-"
    for i in range(N):
        if matrix[i][x] == prev:
            value += 1
        else:
            value = 1
        best = max(best, value)
        prev = matrix[i][x]

    return best


# input
N = int(input())
matrix = [list(input().strip()) for _ in range(N)]

# solve
dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

best = 0
for y in range(N):
    for x in range(N):

        if y == x:
            best = max(best, get_best(y, x))

        for dy, dx in dirs:
            ny, nx = y + dy, x + dx

            if 0 <= ny < N and 0 <= nx < N:
                matrix[y][x], matrix[ny][nx] = matrix[ny][nx], matrix[y][x]
                best = max(best, get_best(y, x))
                matrix[y][x], matrix[ny][nx] = matrix[ny][nx], matrix[y][x]

print(best)
