import sys


sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def is_satisfied(x, y, n):
    start = grid[y][x]
    for j in range(y, y + n):
        for i in range(x, x + n):
            if grid[j][i] != start:
                return False, None
    return True, start


def calculate(x, y, n):
    global w_count, b_count
    is_fine, color = is_satisfied(x, y, n)

    if is_fine:
        if color == 0:
            w_count += 1
        else:
            b_count += 1
        return

    half = n // 2
    calculate(x, y, half)
    calculate(x + half, y, half)
    calculate(x, y + half, half)
    calculate(x + half, y + half, half)


if __name__ == "__main__":
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]

    w_count = 0
    b_count = 0

    calculate(0, 0, N)
    print(w_count)
    print(b_count)
