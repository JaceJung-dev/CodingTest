import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

B = sorted(A)
P = []

for i in range(N):
    idx = B.index(A[i])
    P.append(idx)
    B[idx] = -1

print(*P)

