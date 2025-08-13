import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    if int(N ** 0.5) ** 2 == N:
        print(1)
    else:
        print(0)