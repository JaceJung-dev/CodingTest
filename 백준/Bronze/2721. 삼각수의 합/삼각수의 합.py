import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    w = 0
    for i in range(1, n + 1):
        w += (i * (i + 1) * (i + 2)) // 2
    print(w)
