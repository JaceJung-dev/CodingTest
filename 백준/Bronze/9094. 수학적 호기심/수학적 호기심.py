import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    count = 0
    N, M = map(int, input().split())

    for a in range(1, N):
        for b in range(a + 1, N):
            if (a * a + b * b + M) % (a * b) == 0:
                count += 1
    print(count)
