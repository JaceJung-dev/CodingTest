import sys

input = sys.stdin.readline


# Solution 1
def is_possible(y, x, n):

    for i in range(9):
        if matrix[i][x] == n:
            return False

    for j in range(9):
        if matrix[y][j] == n:
            return False

    for i in range(3):
        for j in range(3):
            if matrix[3 * (y // 3) + i][3 * (x // 3) + j] == n:
                return False

    return True


def search(level):
    # base case
    if level == len(pos):
        for row in matrix:
            print(*row)
        sys.exit(0)

    y, x = pos[level]

    # recursive case
    for n in range(1, 10):
        if is_possible(y, x, n):
            matrix[y][x] = n
            search(level + 1)
            matrix[y][x] = 0


# input
matrix = [list(map(int, input().split())) for _ in range(9)]

# solve
pos = []
for i in range(9):
    for j in range(9):
        if matrix[i][j] == 0:
            pos.append((i, j))

search(0)

# Solution 2


def search(level):

    # base case
    if level == len(pos):
        for row in matrix:
            print(*row)
        sys.exit(0)

    y, x = pos[level]

    # recursive case
    for n in range(1, 10):
        if n not in rows[y] and n not in cols[x] and n not in squares[y // 3][x // 3]:
            matrix[y][x] = n
            rows[y].add(n)
            cols[x].add(n)
            squares[y // 3][x // 3].add(n)

            search(level + 1)

            matrix[y][x] = 0
            rows[y].remove(n)
            cols[x].remove(n)
            squares[y // 3][x // 3].remove(n)


# input
matrix = [list(map(int, input().split())) for _ in range(9)]

# solve
rows = [set() for _ in range(9)]
cols = [set() for _ in range(9)]
squares = [[set() for _ in range(3)] for _ in range(3)]

pos = []
for i in range(9):
    for j in range(9):
        cur = matrix[i][j]
        if cur == 0:
            pos.append((i, j))
        else:
            rows[i].add(cur)
            cols[j].add(cur)
            squares[i // 3][j // 3].add(cur)

search(0)

# Solution 3


def search(level):

    # base case
    if level == len(pos):
        for row in matrix:
            print(*row)
        sys.exit(0)

    y, x = pos[level]

    # recursive case
    for n in range(1, 10):
        if not rows[y][n] and not cols[x][n] and not squares[y // 3][x // 3][n]:
            matrix[y][x] = n
            rows[y][n] = True
            cols[x][n] = True
            squares[y // 3][x // 3][n] = True

            search(level + 1)

            matrix[y][x] = 0
            rows[y][n] = False
            cols[x][n] = False
            squares[y // 3][x // 3][n] = False


# input
matrix = [list(map(int, input().split())) for _ in range(9)]

# solve
rows = [[False] * 10 for _ in range(9)]
cols = [[False] * 10 for _ in range(9)]
squares = [[[False] * 10 for _ in range(3)] for _ in range(3)]
pos = []

for i in range(9):
    for j in range(9):
        cur = matrix[i][j]
        if cur == 0:
            pos.append((i, j))
        else:
            rows[i][cur] = True
            cols[j][cur] = True
            squares[i // 3][j // 3][cur] = True

search(0)
