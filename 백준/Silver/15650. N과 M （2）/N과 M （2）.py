import sys

input = sys.stdin.readline


def combination(idx, level):
    global N, M
    if level == M:
        print(*choose)
        return

    for i in range(idx, N + 1):
        choose.append(i)
        combination(i + 1, level + 1)
        choose.pop()


N, M = map(int, input().split())
choose = []
combination(1, 0)
