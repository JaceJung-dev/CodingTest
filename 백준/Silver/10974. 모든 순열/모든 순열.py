import sys

input = sys.stdin.readline


def permutation(level):
    if level == N:
        print(*selections)
        return

    for i in range(N):
        if check[i]:
            continue

        check[i] = True
        selections.append(i + 1)
        permutation(level + 1)

        selections.pop()
        check[i] = False


N = int(input())
selections = []
check = [False for _ in range(N)]

permutation(0)
