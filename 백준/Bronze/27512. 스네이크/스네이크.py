import sys

input = sys.stdin.readline

N, M = map(int, input().split())

if (N * M) % 2 == 0:
    print(N * M)
else:
    print(N * M - 1)