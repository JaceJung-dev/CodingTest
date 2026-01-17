import sys

input = sys.stdin.readline

N, M, K = map(int, input().split())

if K >= N + M - 1:
    print("YES")
    for j in range(1, N + 1):
        for i in range(M):
            print(j + i, end=" ")
        print()
else:
    print("NO")
