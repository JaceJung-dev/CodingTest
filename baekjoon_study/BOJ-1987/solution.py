import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

# Solution 1


def search(y, x):
    global cnt

    if y < 0 or x < 0 or y >= R or x >= C:
        return

    if matrix[y][x] in seen:
        return

    seen.add(matrix[y][x])

    cnt = max(cnt, len(seen))

    for dy, dx in dirs:
        ny = y + dy
        nx = x + dx

        search(ny, nx)

    seen.remove(matrix[y][x])


# input
R, C = map(int, input().split())
matrix = [input().strip() for _ in range(R)]

# solve
dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
seen = set()
cnt = 0

search(0, 0)

print(cnt)

# Solution 2


def search(y, x):
    global cnt, cur_len

    if y < 0 or x < 0 or y >= R or x >= C:
        return
    if check[ord(matrix[y][x]) - ord("A")]:
        return

    check[ord(matrix[y][x]) - ord("A")] = True
    cur_len += 1

    cnt = max(cnt, cur_len)

    for dy, dx in dirs:
        ny = y + dy
        nx = x + dx

        search(ny, nx)

    cur_len -= 1
    check[ord(matrix[y][x]) - ord("A")] = False


# input
R, C = map(int, input().split())
matrix = [input().strip() for _ in range(R)]

# solve
dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
check = [False] * 26
cnt = 0
cur_len = 0

search(0, 0)

print(cnt)
