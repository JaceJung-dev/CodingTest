import sys

input = sys.stdin.readline

N = int(input())

for i in range(1, 2 * N + 1):
    for j in range(1, 4 * N + 3):
        left = 2 * N - i + 1

        center = 3 * N + 2

        if i <= N:
            gap = i
        else:
            gap = 2 * N - i + 1

        if j == left or j == center - gap or j == center + gap:
            print("*", end="")
        else:
            print(" ", end="")

    print()
